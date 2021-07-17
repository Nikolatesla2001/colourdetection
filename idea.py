import kivy   
from kivy.app import App  
kivy.require('1.9.0')
import copy
from kivy.logger import Logger
from kivy.context import register_context
from kivy.factory import Factory
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
Builder.load_string(""" 
<ScreenOne>: 
    BoxLayout:  
        orientation:'vertical'
        Button: 
            text: "Users Profile" 
            background_color: 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_five' 
        Button:
            text:'Transaction History'
            background_color : 1, 0, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.current = 'screen_two'
<ScreenTwo>: 
    BoxLayout: 
        orientation:'vertical'
        Label:
        	text:'send ₹70 ram'
        Label:
        	text:'send money xxxxxx123 ₹5000'
        Label: 
            text:"Play store purchase₹150" 
        Label:
            text:'eb bill payment in ₹240'
        Label:
            texr:'Airtel prepaid plan ₹219'
        Label:
        	text:'Gift card rewards ₹5'
        Label:
        	text:'swiggy order ₹50'
        Label:
        	text:'send money mathavan ₹45'
        Label:
        	text:'send money worls computers'
        Label:
        	text :' redbus booked ₹155'
        Label:
            text:'jio prepaid plan ₹155'
        Button:
            text:'back'
            size_hint: (.0, .3)
            pos_hint: {'center_y':0.1, 'center_x':0.1,}
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_one'   
<ScreenThree>: 
    BoxLayout: 
        orientation:'vertical'
        Label:
            text: "Ravi, Email: ravi34556@gmail.com, Mobileno: 99954XXXX"
            background_color : 1, 0, 1, 1 
        Button:
            text:'back'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_five'
        Button:
            text:'Transfering'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_six'   
<Screeneighteen>: 
    BoxLayout: 
        orientation:'vertical'
        Label: 
            text: "User Profile"
            text: "Raju, Email: ravi34556@gmail.com, Mobileno: 99954XXXX"     
            background_color : 1, 0, 1, 1 
        Button:
            text:'back'
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.current = 'screen_five'
        Button:
            text:'Transfering'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.current = 'screen_seven'   
<Screennineteen>: 
    BoxLayout: 
        orientation:'vertical'
        Label: 
            text: "User Profile"
            text: "siva,Email: siva34556@gmail.com, Mobileno: 97894XXXX"
            background_color : 1, 0, 1, 1 
        Button:
            text:'back'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.current = 'screen_five' 
        Button:
            text:'Transfering'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.current = 'screen_eight'  
<Screeneleven>: 
    BoxLayout: 
        orientation:'vertical'
        Label: 
            text: "User Profile"
            text: "praveen, Email: praveen98756@gmail.com, Mobileno: 878954XXXX"
            background_color : 1, 0, 1, 1 
        Button:
            text:'back'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_five'
        Button:
            text:'Transfering'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.current = 'screen_nine'   
<Screentwele>: 
    BoxLayout: 
        orientation:'vertical'
        Label:
            text: "User Profile"
            text:"praba, Email; praba986756@gmail.com, Mobileno: 87854XXXX"
            background_color : 1, 0, 1, 1 
           
        Button:
            text:'back'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_five'
        Button:
            text:'Transfering'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.current = 'screen_ten'   
<Screenthirteen>: 
    BoxLayout: 
        orientation:'vertical'
        Label:
            text: "User Profile"
            text:"Karan, Email:karan986756@gmail.com, Mobileno: 754XXXX"
            background_color : 1, 0, 1, 1       
        Button:
            text:'back'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_five'
        Button:
            text:'Transfering'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_twentytwo'   
<Screenfourteen>: 
    BoxLayout: 
        orientation:'vertical'
        Label:
            text: "User Profile"
            text:"ram, Email: ram986756@gmail.com, Mobileno: 73344XXXX"
            background_color : 1, 0, 1, 1   
            
        Button:
            text:'back'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_five'
        Button:
            text:'Transfering'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_five'   
<Screenfifeteen>: 
    BoxLayout: 
        orientation:'vertical'
        Label:
            text: "User Profile"
            text:"raj, Email: raju986756@gmail.com,Mobileno: 73344XXXX"
            background_color : 1, 0, 1, 1   
        Button:
            text:'back'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_five'
        Button:
            text:'Transfering'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_five'   
<Screensixteen>: 
    BoxLayout: 
        orientation:'vertical'
        Label:
            text: "User Profile"
            text:"kaveen, Email: kaveen986756@gmail.com, Mobileno: 89844XXXX"
            background_color : 1, 0, 1, 1   
        Button:
            text:'Transfering'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_twentythree' 
        Button:
            text:'back'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_five'   
<Screenseventeen>: 
    BoxLayout: 
        orientation:'vertical'
        Button:
            text: "User Profile"
            text:"sivaguru, Email:siva986756@gmail.com, Mobileno: 56764XXXX"
            background_color : 1, 0, 1, 1   
        Button:
            text:'back'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_five'
        Button:
            text:'Transfering'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_five'
<Screenfour>: 
    BoxLayout:
        orientation:'vertical' 
        Button: 
            text: "$5000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'   
        Button: 
            text: "$10000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'
        Button: 
            text: "$15000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'      
<ScreenFive>: 
    BoxLayout: 
        orientation:'vertical'
        Button: 
            text: "Karan" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_thirteen' 
        Button: 
            text: "Praba" 
            background_color : 1, 0, 0, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_twele'
        Button: 
            text: "Kaveen" 
            background_color : 1, 0, 1, 1 
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_sixteen'
        Button: 
            text: "Sivaguru" 
            background_color: 1, 1, 0, 1 
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_seven' 
        Button: 
            text: "Siva" 
            background_color : 1, 0, 0, 1 
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_nineteen' 
        Button: 
            text: "Ravi" 
            background_color : 1, 0, 1, 1 
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_three'
        Button: 
            text: "Raju"            
            background_color : 1, 0, 0, 1 
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_eighteen'
        Button:
            text:'back'
            size_hint: (.0, .3)
            pos_hint: {'center_y':0.1, 'center_x':0.1,}
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_one'     
<ScreenNine>: 
    BoxLayout:
        orientation:'vertical' 
        Button: 
            text: "$5000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'   
        Button: 
            text: "$10000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'
        Button: 
            text: "$15000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty' 
        Button:
            text:'back'
            size_hint: (.0, .3)
            pos_hint: {'center_y':0.1, 'center_x':0.1,}
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_one'   
<ScreenTen>: 
    BoxLayout:
        orientation:'vertical' 
        Button: 
            text: "$5000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'   
        Button: 
            text: "$10000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'
        Button: 
            text: "$15000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty' 
<ScreenSix>: 
    BoxLayout:
        orientation:'vertical' 
        Button: 
            text: "$5000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'   
        Button: 
            text: "$10000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'
        Button: 
            text: "$15000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty' 
        Button:
            text:'back'
            size_hint: (.0, .3)
            pos_hint: {'center_y':0.1, 'center_x':0.1,}
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_one' 
<ScreenSeven>:  
    BoxLayout:
        orientation:'vertical' 
        Button: 
            text: "$5000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'   
        Button: 
            text: "$10000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'
        Button: 
            text: "$15000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'  
        Button:
            text:'back'
            size_hint: (.0, .3)
            pos_hint: {'center_y':0.1, 'center_x':0.1,}
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_one'   
<ScreenEight>: 
    BoxLayout:
        orientation:'vertical' 
        Button: 
            text: "$5000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'   
        Button: 
            text: "$10000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'
        Button: 
            text: "$15000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'
        Button:
            text:'back'
            size_hint: (.0, .3)
            pos_hint: {'center_y':0.1, 'center_x':0.1,}
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_one'   
<Screentwentytwo>: 
    BoxLayout:
        orientation:'vertical' 
        Button: 
            text: "$5000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'   
        Button: 
            text: "$10000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'
        Button: 
            text: "$15000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'  
        Button:
            text:'back'
            size_hint: (.0, .3)
            pos_hint: {'center_y':0.1, 'center_x':0.1,}
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_one'
<Screentwentythree>: 
    BoxLayout:
        orientation:'vertical' 
        Button: 
            text: "$5000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'   
        Button: 
            text: "$10000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 

                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'
        Button: 
            text: "$15000" 
            background_color : 0, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1 

                root.manager.current = 'screen_twenty'
        Button:
            text:'back'
            size_hint: (.0, .3)
            pos_hint: {'center_y':0.1, 'center_x':0.1,}
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_one'
<Screentwenty>: 
    BoxLayout: 
        orientation:'vertical'
        Label:
            text: "Amount Successfully transfer"
            background_color : 1, 0, 1, 1  
        Button:
            text:'back'
            background_color : 1, 0, 1, 1
            on_press: 
                root.manager.transition.direction = 'right' 

                root.manager.current = 'screen_one'
""") 
class ScreenOne(Screen): 
    pass
class ScreenTwo(Screen): 
    pass
class ScreenThree(Screen): 
    pass
class ScreenFour(Screen): 
    pass
class ScreenFive(Screen): 
    pass
class ScreenSix(Screen): 
    pass
class ScreenSeven(Screen): 
    pass
class ScreenEight(Screen): 
    pass
class ScreenNine(Screen): 
    pass
class ScreenTen(Screen): 
    pass
class Screeneleven(Screen): 
    pass
class Screentwele(Screen): 
    pass
class Screenthirteen(Screen): 
    pass
class Screenfourteen(Screen): 
    pass
class Screenfifteen(Screen): 
    pass
class Screensixteen(Screen): 
    pass
class Screenseventeen(Screen): 
    pass
class Screeneighteen(Screen): 
    pass
class Screennineteen(Screen): 
    pass
class Screentwenty(Screen): 
    pass
class Screentwentytwo(Screen): 
    pass
class Screentwentythree(Screen): 
    pass
class FactoryException(Exception):
    pass
screen_manager = ScreenManager() 
screen_manager.add_widget(ScreenOne(name ="screen_one")) 
screen_manager.add_widget(ScreenTwo(name ="screen_two")) 
screen_manager.add_widget(ScreenThree(name ="screen_three")) 
screen_manager.add_widget(ScreenFour(name ="screen_four")) 
screen_manager.add_widget(ScreenFive(name ="screen_five")) 
screen_manager.add_widget(ScreenSix(name ="screen_six")) 
screen_manager.add_widget(ScreenSeven(name ="screen_seven")) 
screen_manager.add_widget(ScreenEight(name ="screen_eight")) 
screen_manager.add_widget(ScreenNine(name ="screen_nine")) 
screen_manager.add_widget(ScreenTen(name ="screen_ten")) 
screen_manager.add_widget(Screeneleven(name ="screen_leven")) 
screen_manager.add_widget(Screentwele(name ="screen_twele")) 
screen_manager.add_widget(Screenthirteen(name ="screen_thirteen")) 
screen_manager.add_widget(Screenfourteen(name ="screen_fourteen")) 
screen_manager.add_widget(Screenfifteen(name ="screen_fifteen")) 
screen_manager.add_widget(Screensixteen(name ="screen_sixteen")) 
screen_manager.add_widget(Screenseventeen(name ="screen_seventeen")) 
screen_manager.add_widget(Screeneighteen(name ="screen_eighteen")) 
screen_manager.add_widget(Screennineteen(name ="screen_nineteen")) 
screen_manager.add_widget(Screentwenty(name ="screen_twenty")) 
screen_manager.add_widget(Screentwentytwo(name ="screen_twentytwo")) 
screen_manager.add_widget(Screentwentythree(name ="screen_twentythree")) 
class ScreenApp(App): 
    def build(self): 
        return screen_manager
sample_app = ScreenApp() 
sample_app.run() 