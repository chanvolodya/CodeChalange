import sys
from notebook import Note, Notebook 

class Menu(object):
	"""docstring for Menu"""
	def __init__(self):
		self.notebook = Notebook()
		self.choices = {
			"1": self.show_notes,
			"2": self.search_notes,
			"3": self.add_note,
			"4": self.modify_note,
			"5": self.quit
		}
	def display_menu(self):
		print("""
			Notebook Menu
			1. Show all notes
			2. Search notes
			3. Add note
			4. Modify note
			5. Quit
			""")
	def run(self):
		''' Display menu and respond choices'''
		while True:
			self.display_menu()
			choice = input("Enter an choice ")
			action = self.choices.get(choice)
			if action:
				action()
			else:
				print(f"{choice} is not avaliable choice ")

	def show_notes(self,notes = None):
		if not notes:
			notes = self.notebook.notes

		for note in notes:
			print(f"Id: {note.id}, Tags: {note.tags}, Content: {note.memo}")

	def search_notes(self):
		filter = input("Enter memo you want to search ")
		result = self.notebook.search(filter)
		self.show_notes(result)

	def add_note(self):
		memo = input("Enter memo note ")
		tag =input("Enter tag of note ")
		self.notebook.new_note(memo,tag)
		print("Note has been add")

	def modify_note(self):
		id = input("Enter a note id  ")
		memo = input("Enter a memo ")
		tags = input("Enter tags: ")
		if memo:
			self.notebook.modify_memo(id, memo)
		if tags:
			self.notebook.modify_tags(id,tags)

	def quit():
		print("Thanks for using your notebook today!!Love you")
		sys.exit(0)

if __name__ == '__main__':
	Menu().run()