import carla

clint = carla.Client('localhost', 2000)

world = clint.get_world()
spawn_points = world.get_map().get_spawn_points()

vehicle_bp = world.get_blueprint_library().filter('*firetruck*')
start_point = spawn_points[0]
vehicle = world.try_spawn_actor(vehicle_bp[0], start_point)

vehicle_pos = vehicle.get_transform()
print(vehicle_pos)
