import bpy

class UI(bpy.types.Panel):
  bl_label = "my panel"
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  
  def draw(self, context):
    self.layout.operator("my.button")
    

class MyButton(bpy.types.Operator):
  bl_idname = "my.button"
  bl_label = "text"

#####################################################################################
  my_float = bpy.props.FloatProperty(name="Some Floating Point")
  my_bool = bpy.props.BoolProperty(name="Toggle Option")
  my_string = bpy.props.StringProperty(name="String Value")
  
  def execute(self, context):
    message = "%f, %d, '%s'" % (self.my_float, self.my_bool, self.my_string)
    print(message)
    return{'FINISHED'}

  def invoke(self, context, event):
    return context.window_manager.invoke_props_dialog(self)

#####################################################################################

classes = (
  UI,
  MyButton
)

for cls in classes:
  bpy.utils.register_class(cls)
  
''' 登録を解除する場合
for cls in reversed(classes):
  bpy.utils.unregister_class(cls)
'''