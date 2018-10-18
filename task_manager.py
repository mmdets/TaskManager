import sys
import kivy
import datetime
import time
import sqlite3
import re
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.uix.popup import Popup
from KivyCalendar import CalendarWidget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ReferenceListProperty,\
	StringProperty, ObjectProperty

tasks = sqlite3.connect("database.db")
cursor = tasks.cursor()

class MainScreen(Screen):
	content = StringProperty(None)
	status = StringProperty(None)
	listTask = StringProperty(None)
	count = NumericProperty(None)

	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)
		self.content = "Welcome to the Task Manager!\n\n[i]Start by doing what is necessary;\nthen do what is possible;\nand suddenly you are doing the impossible.[/i]\nFrancis Of Assisi" 
		sql = "SELECT * FROM tasks WHERE status LIKE 'True'"
		cursor.execute(sql)
		self.listTask = re.sub('[!"[)()]', '', str(cursor.fetchall()))
		self.listTask = re.sub('[]]', '', self.listTask)
		
class AddScreen(Screen):
	pass

class CalendarScreen(Screen):
	def Calendar(self):
		self.cal = CalendarWidget()

class ScreenScreen(Screen):
	pass

class HomeScreen(Screen):
	pass

class HobbyScreen(Screen):
	pass

class FitnessScreen(Screen):
	pass

class TaskScreen(Screen):
	category = StringProperty(None)
	def setDate(self):
		self.cal = CalendarWidget(as_popup=True)
		self.popup = Popup(title='Calendar', content=self.cal, size_hint=(1, 1))
		self.popup.open()
	
	def save(self, category, description, date_task, time_task):
		params = (str(category), str(description), str(date_task), str(time_task), 'True')
		cursor.execute("""INSERT INTO tasks
		VALUES (?, ?, ?, ?, ?)"""
		   				, params)
		tasks.commit()

class ScreenManagerApp(App):
	title = "Task manager"

	def build(self):
		root = ScreenManager()
		root.add_widget(MainScreen(name='Main'))
		root.add_widget(AddScreen(name='Add'))
		root.add_widget(CalendarScreen(name='Calendar'))
	#	root.add_widget(ScreenScreen(name='Screen'))
		root.add_widget(HomeScreen(name='Home'))
		root.add_widget(HobbyScreen(name='Hobby'))
		root.add_widget(FitnessScreen(name='Fitness'))
		root.add_widget(TaskScreen(name='Task'))
		return root

if __name__ == '__main__':
	ScreenManagerApp().run()