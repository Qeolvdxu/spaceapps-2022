extends Button


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
export (String) var scene_path

func _on_StartGameButton_pressed():
	get_tree().change_scene(scene_path)

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func _on_AboutButton_pressed():
	get_tree().change_scene(scene_path)
