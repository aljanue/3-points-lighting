# Author: Alberto Jativa
# version ='1.0'
# ----------------------------------------------------------------------------------------------
""" 
Script that implements the interface to create three-point lighting around an object
"""
# ----------------------------------------------------------------------------------------------
# Addon information
# ----------------------------------------------------------------------------------------------
bl_info = {
    "name": "3 Points Lighting",
    "author": "aljanue",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Lighting > Lighting",
    "description": "Illuminate a 3D object with a three-point based lighting",
    "category": "Lighting",
}
# ----------------------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------------------
import bpy
import os
import sys

dir = os.path.dirname(os.path.realpath(__file__))
if not dir in sys.path:
    sys.path.append(dir)
    
import lighting


# Class to create a panel with different settings to illuminate the scene
class LightingPanel(bpy.types.Panel):
    """
    Creates a panel to generate the lighting of a scene
    """
    bl_label = "3 POINTS Lighting"
    bl_idname = "OBJECT_PT_Lighting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Lighting"

    def draw(self, context):
        layout = self.layout

        obj = context.object
        scene = context.scene
        
        row = layout.row()
        row.label(text="1. Select an object")
        
        row = layout.row()
        row.label(text="2. Adjust the parameters")
        
        row = layout.row()
        row.label(text="Scene size", icon="EMPTY_AXIS")
        
        row = layout.row()
        row.prop(scene, "x")
        row.prop(scene, "y")
        row.prop(scene, "z")
        
        row = layout.row()
        row.label(text="Lights intensity", icon='LIGHT')
        
        row = layout.row()
        row.prop(scene, "intensity")
                
        row = layout.row()
        row.label(text="3. Apply the lighting")
        
        row = layout.row()
        row.operator("object.generate_lighting")
        
class GenerateLightingOperator(bpy.types.Operator):
    """
    Generates a scene with the three lights around the object
    """
    bl_idname = "object.generate_lighting"
    bl_label = "Apply"

    def execute(self, context):
        lighting.GenerateLights()
        return{'FINISHED'}
    
def register():
    """
    Blender function used to register and enable all classes, custom properties,
    operators and panels that are part of the lighting.
    This function is called when the plugin is activated from Blender.
    """
    bpy.types.Scene.x = bpy.props.FloatProperty(name = "Scene x size",
                                                                description="Scene x size",
                                                                min = 0.0001,
                                                                default = 50)
    bpy.types.Scene.y = bpy.props.FloatProperty(name = "Scene y size",
                                                                description="Scene y size",
                                                                min = 0.0001,
                                                                default =50)
    bpy.types.Scene.z = bpy.props.FloatProperty(name = "Scene z size",
                                                                description="Scene z size",
                                                                min = 0.0001,
                                                                default =20)
    bpy.types.Scene.intensity = bpy.props.FloatProperty(name = "Main light intensity",
                                                                description="Main light intensity",
                                                                min = 0,
                                                                default = 10000)
                                                                
    bpy.utils.register_class(LightingPanel)
    bpy.utils.register_class(GenerateLightingOperator)

    
def unregister():
    """
    Blender function used to perform cleanup and unregister the classes
    and custom properties that were previously registered in the plugin through
    the register() function. 
    This function is called when the plugin is deactivated or removed from Blender.
    """
    # Classes and operators are unregistered when the plugin is deactivated or removed
    bpy.utils.unregister_class(LightingPanel)
    bpy.utils.unregister_class(GenerateLightingOperator)
    
    del bpy.types.Scene.x
    del bpy.types.Scene.y
    del bpy.types.Scene.z
    del bpy.types.Scene.intensity
    
if __name__ == "__main__":
    register()