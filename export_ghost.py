import bpy
import os

print("--- EXPORTING GHOST TO GLB ---")
bpy.ops.object.select_all(action='DESELECT')

ghost_obj = bpy.data.objects.get('tripo_node_c5d1eb2d-0b21-4fd8-ad86-d06fc083428f')
if not ghost_obj:
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            ghost_obj = obj
            break

if ghost_obj:
    print(f"Found ghost object: {ghost_obj.name}")
    ghost_obj.select_set(True)
    bpy.context.view_layer.objects.active = ghost_obj

output_path = r"C:\Users\лахушка\.gemini\antigravity\scratch\prototype\ghost.glb"

bpy.ops.export_scene.gltf(
    filepath=output_path,
    export_format='GLB',
    use_selection=True,
    export_apply=True,
    export_materials='EXPORT'
)

if os.path.exists(output_path):
    print("SUCCESS GHOST GLB size:", os.path.getsize(output_path), "bytes")
else:
    print("ERROR: ghost.glb not found")
