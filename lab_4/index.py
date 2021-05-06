class Screen:
	resolution = []

	def setResolution(self, x, y):
		self.resolution = [x, y]
		print("Ustawiłem rozdzielczość na ", x, "x", y)

	def showPicture():
		print("Pokazuję zdjęcie")

	def freeze(self):
		print("Zamroziłem obraz")

	def unfreeze(self):
		print("Odmroziłem obraz")

screen = Screen()
screen.setResolution(1920, 1080)
screen.freeze();
screen.unfreeze();