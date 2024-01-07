import bpy
from mathutils import Vector

"""Function that creates 3-point based lighting in a scene 
within an empty object with dimensions defined by the user."""
def GenerateLights():
    # Variables
    scene_size_x = bpy.context.scene.x
    scene_size_y = bpy.context.scene.y
    scene_size_z = bpy.context.scene.z
    intensity = bpy.context.scene.intensity

    # Save the object to access its properties later
    main = bpy.context.active_object

    # Add empty object
    bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=main.location, scale=(1, 1, 1))

    # Get the reference to the empty object
    empty_object = bpy.context.active_object
    empty_object.name = "3_POINTS_LIGHT"
    empty_object.scale = Vector([scene_size_x/2, scene_size_y/2, scene_size_z/2])

    ## MAIN LIGHT
    # Calculate the location of the main light
    key_light_location = main.location + Vector([(scene_size_x-scene_size_x/5)/2, -(scene_size_y-scene_size_y/5)/2, 0])
    # Create main light
    key_light_data = bpy.data.lights.new(name="KeyLight", type='AREA')
    key_light = bpy.data.objects.new(name="KeyLight", object_data=key_light_data)
    bpy.context.collection.objects.link(key_light)

    # Set the location and scale 
    key_light.location = key_light_location
    key_light.scale = Vector([main.dimensions.x*(scene_size_x/2), main.dimensions.z*(scene_size_z/2), main.dimensions.y])

    # Add Track To constraint to the main light
    track_constraint = key_light.constraints.new(type='TRACK_TO')
    track_constraint.target = main
    track_constraint.track_axis = 'TRACK_NEGATIVE_Z'
    track_constraint.up_axis = 'UP_Y'
    key_light.data.energy = intensity

    # Parent object
    empty_object.select_set(True)
    bpy.ops.object.parent_set(type='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    key_light.select_set(True)
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

    ## FILL LIGHT
    # Calculate the location of the fill light
    fill_light_location = main.location + Vector([-(scene_size_x-scene_size_x/5)/2, -(scene_size_y-scene_size_y/5)/2, 0])
    # Create fill light
    fill_light_data = bpy.data.lights.new(name="FillLight", type='AREA')
    fill_light = bpy.data.objects.new(name="FillLight", object_data=fill_light_data)
    bpy.context.collection.objects.link(fill_light)

    # Set the location and scale of the fill light
    fill_light.location = fill_light_location
    fill_light.scale = Vector([main.dimensions.x*(scene_size_x)/2, main.dimensions.z*(scene_size_z/2), main.dimensions.y])

    # Add Track To constraint to the fill light object
    track_constraint = fill_light.constraints.new(type='TRACK_TO')
    track_constraint.target = main
    track_constraint.track_axis = 'TRACK_NEGATIVE_Z'
    track_constraint.up_axis = 'UP_Y'
    fill_light.data.energy = intensity*0.6

    # Parent object
    empty_object.select_set(True)
    bpy.ops.object.parent_set(type='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    fill_light.select_set(True)
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

    ## BACK LIGHT
    # Calculate the location of the back spot light
    back_light_location = main.location + Vector([0, 0, main.dimensions.z/2 + 8])

    # Create back spot light
    back_light_data = bpy.data.lights.new(name="BackLight", type='SPOT')
    back_light = bpy.data.objects.new(name="BackLight", object_data=back_light_data)
    bpy.context.collection.objects.link(back_light)

    # Set the location and scale of the back spot light
    back_light.location = back_light_location
    back_light.scale.x = main.scale.x/1.5
    back_light.scale.y = main.scale.y/1.5

    # Set the cone of the back spot light
    back_light.data.spot_blend = 1 
    back_light.data.energy = 200

    # Add Track To constraint to the back light object
    track_constraint = back_light.constraints.new(type='TRACK_TO')
    track_constraint.target = main
    track_constraint.track_axis = 'TRACK_NEGATIVE_Z'
    track_constraint.up_axis = 'UP_Y'

    # Parent objects
    empty_object.select_set(True)
    bpy.ops.object.parent_set(type='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    back_light.select_set(True)
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)