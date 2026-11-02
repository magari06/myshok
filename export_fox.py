import bpy
import os

print("--- EXPORTING FOX TO GLB ---")
bpy.ops.object.select_all(action='DESELECT')

# Find FoxModel
fox = bpy.data.objects.get('FoxModel')
if not fox:
    for obj in bpy.data.objects:
        if 'fox' in obj.name.lower():
            fox = obj
            break

if fox:
    print(f"Found fox object: {fox.name}, type: {fox.type}")
    fox.select_set(True)
    bpy.context.view_layer.objects.active = fox
else:
    print("Warning: FoxModel not found specifically, selecting all meshes except StudioFloor")
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and 'floor' not in obj.name.lower():
            obj.select_set(True)

output_path = r"C:\Users\лахушка\.gemini\antigravity\scratch\prototype\fox.glb"

bpy.ops.export_scene.gltf(
    filepath=output_path,
    export_format='GLB',
    use_selection=True,
    export_apply=True,
    export_materials='EXPORT'
)

if os.path.exists(output_path):
    print("SUCCESS: GLB file size:", os.path.getsize(output_path), "bytes")
else:
    print("ERROR: GLB file not found")
