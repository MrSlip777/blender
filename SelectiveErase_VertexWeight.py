import bpy

# アドオンについての説明
bl_info = {
    "name": "Selectively remove vertex weights",
    "author": "slip",
    "version": (1, 0),
    "blender": (2, 81, 0),
    "location": "location",
    "description": "Selectively remove vertex weights",
    "warning": "warning",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "http://hogehoge2.com",
    "category": "Object"
}

# UI(ボタンを構築するクラス)
class UI(bpy.types.Panel):
  bl_label = "vertex weights"
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"

  def draw(self, context):
    self.layout.operator("selectively_remove_vertex_weights.button")



# アドオンのクラス
class SelectivelyRemoveVertexWeights(bpy.types.Operator):

    #アクティブなオブジェクトを取得    
    tempObject = bpy.context.object
    targetObject_string = tempObject.name

    #targetObject_string = ""
    bl_idname = "selectively_remove_vertex_weights.button" # ID
    bl_label = "RemoveWeight_" +  targetObject_string# メニューに追加されるラベル
    bl_description = "selectively remove vertex weights" # 関数の説明
    bl_options = {'REGISTER', 'UNDO'} # 処理の属性

    vg_name1 = bpy.props.StringProperty(name = "ProtectVertexGroup1")
    vg_name2 = bpy.props.StringProperty(name = "ProtectVertexGroup2")
    vg_name3 = bpy.props.StringProperty(name = "ProtectVertexGroup3")
    vg_name4 = bpy.props.StringProperty(name = "ProtectVertexGroup4")
    vg_name5 = bpy.props.StringProperty(name = "ProtectVertexGroup5")
    vg_name6 = bpy.props.StringProperty(name = "ProtectVertexGroup6")
    vg_name7 = bpy.props.StringProperty(name = "ProtectVertexGroup7")
    vg_name8 = bpy.props.StringProperty(name = "ProtectVertexGroup8")
    vg_name9 = bpy.props.StringProperty(name = "ProtectVertexGroup9")
    vg_name10 = bpy.props.StringProperty(name = "ProtectVertexGroup10")

    temp_vg_s = tempObject.vertex_groups

    for vg in temp_vg_s:
        if vg.name = vg_name1:
            print(vg.name)
            print(vg.index)
            break

    def execute(self, context):

        if self.targetObject_string != "":

            obj_s = bpy.data.objects

            for obj in obj_s:
                if obj.name == self.targetObject_string:
                    vg_s = obj.vertex_groups
                    break

            obj = tempObject

            for v in obj.data.vertices:
                for vge in v.groups:
                    #bpy.context.object.active_index = vge.group
                    if vge.group != 100:
                        vge.weight = 0.0
                        
        else:
            pass

        print("selectively remove vertex weights End") # コンソールにログ出力
        self.report({'INFO'}, "selectively remove vertex weights End")
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)



# クラスをまとめる
classes = (
  UI,
  SelectivelyRemoveVertexWeights
)

# まとめたクラスを一度に登録
register, unregister = bpy.utils.register_classes_factory(classes)