# 3 Points Lighting Addon for Blender

This addon for Blender allows you to create a three-point lighting setup around an object in a 3D scene. Three-point lighting is a common technique in photography and cinematography that uses three light sources to illuminate an object from different angles, providing balanced lighting and avoiding harsh shadows.

## Installation

1. Click on `<> Code` and Download the folder as `.zip`.
2. Compress the `3_points_lighting` folder into a `.zip` file.
3. Open Blender and go to `Edit > Preferences`.
4. In the preferences window, select the `Add-ons` tab.
5. Click on `Install...` and locate the `.zip` file you compressed.
6. Once installed, make sure the addon is enabled by checking the box next to its name.

## Usage

This addon adds a panel in the 3D Viewport. To use it, follow these steps:

1. Select an object in your 3D scene.
2. Adjust the dimensions around the object and the intensity of the main light.
3. Click on the "Apply" button to generate the three-point lighting around your object.
4. Now, you can customize the lights by adjusting them all at once or independently.

How it works

1. **Variable Definition:** The first lines define the variables `scene_size_x`, `scene_size_y`, `scene_size_z`, and `intensity` which represent the dimensions of the scene and the intensity of the light, respectively. These values are obtained from the properties of the current scene in Blender.

2. **Empty Object Creation:** An empty object is created at the location of the current active object. This empty object will be used to contain the lights.

3. **Empty Object Configuration:** The name of the empty object is set to "3_POINTS_LIGHT" and its scale is adjusted based on the dimensions of the scene.

4. **Key Light Creation:** The location of the key light is calculated based on the dimensions of the scene. Then, a new light of type 'AREA' is created at that location and is named "KeyLight".

5. **Key Light Configuration:** The location and scale of the key light are set. Then, a 'TRACK_TO' type constraint is added to the light, which makes the light always point to the active object. Finally, the energy of the light (i.e., its intensity) is set to the value of the `intensity` variable.

6. **Parenting:** Finally, the empty object is set as the active object and is selected. This sets the stage for the following lights to be added within the same empty object.

7. **Fill Light Creation and Configuration:** Similar steps are followed to create and configure the fill light. The fill light is positioned opposite to the key light and its intensity is set to 60% of the key light's intensity.

8. **Back Light Creation and Configuration:** The back light is created as a 'SPOT' type light and is positioned above the active object. Its scale is set to be smaller than the active object's scale and its intensity is set to a fixed value of 200.
