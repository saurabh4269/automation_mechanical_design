import win32com.client as wc

inv = wc.GetActiveObject('Inventor.Application')
# print(inv)

# # Create a part document
# inv_part_document = inv.Documents.Add(12290, inv.FileManager.GetTemplateFile(12290, 8962))

# # inv_part_document = inv.ActiveDocument
# # print(inv_part_document)

# # #set a reference to part component definition
# part_comp_definition = inv_part_document.ComponentDefinition

# # print(dir(part_comp_definition))

# #create a sketch

# # print(part_comp_definition.WorkPlanes.Item(3).Name)
# sketch = part_comp_definition.Sketches.Add(part_comp_definition.WorkPlanes.Item(3))

# tg = inv.TransientGeometry
# # print(tg)

# sketch.SketchLines.AddAsTwoPointCenteredRectangle(tg.CreatePoint2d(0,0), tg.CreatePoint2d(8,3))

# inv.ActiveView.GoHome()

# #create an extrusion

# solid_profile = sketch.Profiles.AddforSolid()

# #creating the feature
# ext_solid_def = part_comp_definition.Features.ExtrudeFeatures.CreateExtrudeDefinition(solid_profile, 20481)
# ext_solid_def.SetDistanceExtent(1, 20994)


# part_comp_definition.Features.ExtrudeFeatures.Add(ext_solid_def)

# #add holes 2.5 mm holes / 5mm away from the edges

# #create a new sketch with the position for the holes (workplane)
# hole_sketches = part_comp_definition.Sketches.Add(part_comp_definition.WorkPlanes.Item(3))
# #create an object collection
# holes_centers = inv.TransientObjects.CreateObjectCollection()
# #add 4 points as hole centers
#     # (-7.5, -2.5)
#     # (-7.5, 2.5)
#     # (7.5, -2.5)
#     # (7.5, 2.5)
# holes_centers.Add(hole_sketches.Sketchpoints.Add(tg.CreatePoint2d(-7.5,-2.5)))
# holes_centers.Add(hole_sketches.Sketchpoints.Add(tg.CreatePoint2d(-7.5,2.5)))
# holes_centers.Add(hole_sketches.Sketchpoints.Add(tg.CreatePoint2d(7.5,-2.5)))
# holes_centers.Add(hole_sketches.Sketchpoints.Add(tg.CreatePoint2d(7.5,2.5)))

# #add the hole feature to the part component definition
# part_comp_definition.Features.HoleFeatures.AddDrilledByThroughAllExtent(holes_centers, "5 mm", 20993)

# # ===adding fillets to the corners(next in line)
# # feature creation process
#     # a fillet of 3mm

#     # create a feature definition object
#     # add details of the features to be added
#     # add the features to the feature collection

# edges1 = part_comp_definition.SurfaceBodies.Item(1).Faces.Item(6).Edges.Item(2)
# edges2 = part_comp_definition.SurfaceBodies.Item(1).Faces.Item(6).Edges.Item(4)
# edges3 = part_comp_definition.SurfaceBodies.Item(1).Faces.Item(8).Edges.Item(2)
# edges4 = part_comp_definition.SurfaceBodies.Item(1).Faces.Item(8).Edges.Item(4)

# edge_collection_side = inv.TransientObjects.CreateEdgeCollection()
# side_fillet_definition = part_comp_definition.Features.FilletFeatures.CreateFilletDefinition()

# edge_collection_side.Add(edges1)
# edge_collection_side.Add(edges2)
# edge_collection_side.Add(edges3)
# edge_collection_side.Add(edges4)

# side_fillet_definition.AddConstantRadiusEdgeSet(edge_collection_side, 0.3)
# part_comp_definition.Features.FilletFeatures.Add(side_fillet_definition)


# #save the part
# # inv.ActiveDocument.SaveAs("F:\@\\base_plate.ipt", False)


# Get user inputs
radius = float(input("Enter the radius of the cylinder (in cm): "))
height = float(input("Enter the height of the cylinder (in mm): "))
angle = float(input("Enter the angle for extrusion (in degrees, 0 for none): "))

#create a pin
    # create the part
inv_part_document = inv.Documents.Add(12290, inv.FileManager.GetTemplateFile(12290, 8962))
pin_comp_def = inv_part_document.ComponentDefinition

    # define sketch
pin_sketch = pin_comp_def.Sketches.Add(pin_comp_def.WorkPlanes.Item(3))

    # transient
tg = inv.TransientGeometry

circle_sketch = pin_sketch.SketchCircles

circle_sketch.AddByCenterRadius(tg.CreatePoint2d(0,0), radius)
solid_profile = pin_sketch.Profiles.AddforSolid()

# # Add a circle segment sketch
# lines = sketch.SketchLines
# point1 = tg.CreatePoint2d(0, 0)
# point2 = tg.CreatePoint2d(radius * cos(angle * pi / 180), radius * sin(angle * pi / 180))
# lines.AddByTwoPoints(point1, tg.CreatePoint2d(radius, 0))
# lines.AddByTwoPoints(point1, point2)
# arc = sketch.SketchArcs.AddByCenterStartEndPoint(point1, lines.Item(1).EndSketchPoint, lines.Item(2).EndSketchPoint)
# profile = sketch.Profiles.AddForSolid()


extrude_solid_def = pin_comp_def.Features.ExtrudeFeatures.CreateExtrudeDefinition(solid_profile, 20481)
extrude_solid_def.SetDistanceExtent("height", 20994)

pin_comp_def.Features.ExtrudeFeatures.Add(extrude_solid_def)
# inv.ActiveDocument.SaveAs("C:\\pin.ipt", False)
