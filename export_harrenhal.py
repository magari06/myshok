import bpy
import os

print("--- EXPORTING HARRENHAL CASTLE ARCHITECTURE TO GLB ---")
bpy.ops.object.select_all(action='DESELECT')

target_collections = [
    '05_Titan_Keeps',
    '03_Outer_Walls_and_Gatehouse',
    '04_Middle_Wards_and_Ruins',
    '06_Skybridges_and_Details',
    '08_Scaffolding_and_Cranes'
]

selected_count = 0
for col_name in target_collections:
    col = bpy.data.collections.get(col_name)
    if col:
        for obj in col.all_objects:
            if obj.type == 'MESH':
                obj.select_set(True)
                selected_count += 1

print(f"Selected {selected_count} architecture objects for Harrenhal GLB export.")

output_path = r"C:\Users\лахушка\.gemini\antigravity\scratch\prototype\harrenhal.glb"

bpy.ops.export_scene.gltf(
    filepath=output_path,
    export_format='GLB',
    use_selection=True,
    export_apply=True,
    export_materials='EXPORT'
)

if os.path.exists(output_path):
    print("SUCCESS HARRENHAL GLB size:", os.path.getsize(output_path), "bytes")
else:
    print("ERROR: harrenhal.glb not found")
