import bpy

verts = [[-1.0, -1.0,  1.0], [1.0, -1.0,  1.0], [1.0, 1.0,  1.0], [-1.0, 1.0,  1.0],
         [-1.0, -1.0, -1.0], [1.0, -1.0, -1.0], [1.0, 1.0, -1.0], [-1.0, 1.0, -1.0], ]
faces = [[0,1,2,3], [0,4,5,1], [1,5,6,2], [2,6,7,3], [0,3,7,4], [4,7,6,5]]

msh = bpy.data.meshes.new(name="cubemesh")
#msh = bpy.data.meshes.new("cubemesh")
msh.from_pydata(verts, [], faces)
msh.update()
obj = bpy.data.objects.new(name="cube", object_data=msh)
#obj = bpy.data.objects.new("cube", msh)
scene = bpy.context.scene
#scene.objects.link(obj)
scene.collection.objects.link(obj)

bone_list = ["bone1", "bone2"]
weight_map = {"bone1":[1.0]*4+[0.0]*4, # [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
              "bone2":[0.0]*4+[1.0]*4,
              }

vg_list = [] # VertexGroupのリスト
# vertex groupの作成
for bname in bone_list:
    obj.vertex_groups.new(name=bname)
    #obj.vertex_groups.new(bname)
    vg_list.append(obj.vertex_groups[-1])

# VertexGroup経由での設定
for vg in vg_list:
    weights = weight_map[vg.name]
    for vidx, w in enumerate(weights):
        if w != 0.0:
            vg.add([vidx], w, 'REPLACE')