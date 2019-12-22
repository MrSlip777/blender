bone_list = ["bone1", "bone2"]
weight_map = {"bone1":[1.0]*4+[0.0]*4, # [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
              "bone2":[0.0]*4+[1.0]*4,
              }
obj = bpy.data.objects
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