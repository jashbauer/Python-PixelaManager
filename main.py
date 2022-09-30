from pixela_management import PixelaManager

manager = PixelaManager()

# -------- USER PARAMS EXAMPLE --------------------
user_parameters = {
    "token": "<token>",
    "username": "<username>",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# -------- GRAPH PARMS EXAMPLE ----------------------
graph_config = {
    "id": "graph1",
    "name": "Coding Time",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

# CREATES USER
manager.create_user(user_parameters)

# CREATES GRAPH
manager.create_graph(g_parameters=graph_config)

# POSTS PIXEL
manager.post_pixel(quantity="<int / float - Depends on your graph config>")

# UPDATES PIXEL
manager.update_pixel(new_quantity="<quantity to update>", date="<pixel date>")

# DELETES PIXEL
manager.delete_pixel(date="<pixel date>")

# CHECKS GRAPH INFO
manager.get_graph_def()

# YOU CAN ALWAYS CHANGE USER / GRAPH BY CHANGING THE CLASS' PROPERTIES:
# User Data
print(manager.USERNAME)
print(manager.PX_TOKEN)

# Graph Data
print(manager.GRAPH_ID)
