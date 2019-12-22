import bpy

# アドオンについての説明
bl_info = {
    "name": "sample: add-onTest",
    "author": "ssss",
    "version": (2, 0),
    "blender": (2, 80, 0),
    "location": "location",
    "description": "sample",
    "warning": "warning",
    "support": "TESTING",
    "wiki_url": "http://hogehoge.com",
    "tracker_url": "http://hogehoge2.com",
    "category": "Object"
}

# UI(ボタンを構築するクラス)
class UI(bpy.types.Panel):
  bl_label = "add sphere panel"
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  
  def draw(self, context):
    self.layout.operator("add_sphere_object.button")

# アドオンのクラス
class AddSphere(bpy.types.Operator):
    bl_idname = "add_sphere_object.button" # ID
    bl_label = "Add Sphere" # メニューに追加されるラベル
    bl_description = "Add Sphere" # 関数の説明
    bl_options = {'REGISTER', 'UNDO'} # 処理の属性

    def execute(self, context):
        bpy.ops.mesh.primitive_ico_sphere_add()
        print("Add Sphere End") # コンソールにログ出力
        self.report({'INFO'}, "Add Sphere End")
        return {'FINISHED'}

# クラスをまとめる
classes = (
  UI,
  AddSphere
)

# まとめたクラスを一度に登録
register, unregister = bpy.utils.register_classes_factory(classes)