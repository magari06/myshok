import bpy
import os

print("--- ANALYZING HARRENHAL COLLECTIONS ---")
for col in bpy.data.collections:
    mesh_count = sum(1 for o in col.all_objects if o.type == 'MESH')
    poly_count = sum(len(o.data.polygons) for o in col.all_objects if o.type == 'MESH' and o.data)
    print(f"Col: {col.name} -> {mesh_count} meshes, {poly_count} polys")
