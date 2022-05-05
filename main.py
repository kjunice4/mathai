#Bundled App
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import numpy as np
import sympy as sym
from colorama import Back, Style 
from sympy import Limit, Symbol, S, diff, integrate
import math
from android.billing import BillingService
from kivy.clock import Clock

class MyBillingService(object):
    def __init__(self):
        super(MyBillingService, self).__init__()
        # Start the billing service, and attach our callback
        self.service = BillingService('billing_callback')
        # Start a clock to check billing service message every second
        Clock.schedule_interval(self.service.check, 1)
    def billing_callback(self, action, *largs):
        '''Callback that will receive all the events from the Billing service'''
        if action == BillingService.BILLING_ACTION_ITEMSCHANGED:
            items = largs[0]
            if 'org.ksquared.bundled_app' in items:
                print("Congratulations, you have a premium acess")
            else:
                print("Unfortunately, you don't have premium access")
    def buy(self, sku):
        # Method to buy something.
        self.service.buy(sku)
    def get_purchased_items(self):
        # Return all the items purchased
        return self.service.get_purchased_items()
# Note: start the service at the start, and never twice!
bs = MyBillingService()
bs.buy('org.ksquared.bundled_app')
# Later, when you get the notification that items have been changed, you
# can still check all the items you bought:
print(bs.get_purchased_items())


#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "KSquared Mathematics"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "All Calculators"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"
                
""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
                
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Algebra"
                
            Button:
                text: "Domain and Range"
                font_size: '20sp'
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Domain_and_Range"
                    root.manager.transition.direction = "left"    
                    
            Button:
                text: "Exponents Calculator"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0, 1, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Exponents_steps"
                    root.manager.transition.direction = "left"    
            
            Button:
                text: "FOIL Method"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0, 1, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "FOIL"
                    root.manager.transition.direction = "left"
            
            Button:
                text: "PEMDAS"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0, 1, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "PEMDAS"
                    root.manager.transition.direction = "left"       
            
            Button:
                text: "Quadratic Calculator"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0, 1, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Quadratic_Formula_Solver"
                    root.manager.transition.direction = "left"
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Basic"
            
            Button:
                text: "Basic Calculator"   
                font_size: '20sp'
                background_color: 1, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Basic"
                    root.manager.transition.direction = "left" 
            
            Button:
                text: "Fractions Calculator"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 1, 0, 1, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Fractions"
                    root.manager.transition.direction = "left"    
                    
            Button:
                text: "Percentage Calculator"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 1, 0, 1, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Percentage_Calculator"
                    root.manager.transition.direction = "left" 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                background_color: 0, 0, 1, 1
                text: "Calculus"
                
            Button:
                text: "Derivatives Calculator"
                font_size: '20sp'
                background_color: 0, 1, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Derivatives"
                    root.manager.transition.direction = "left" 
                    
            Button:
                text: "Integration Calculator"
                font_size: '20sp'
                background_color: 0, 1, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Integration"
                    root.manager.transition.direction = "left"
                    
            Button:
                text: "Limits Calculator"
                font_size: '20sp'
                background_color: 0, 1, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Limits"
                    root.manager.transition.direction = "left"
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Converters"
            
            Button:
                text: "Decimals Converter"
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1, 0, 1
                height: 200
                on_release:
                    app.root.current = "Decimals_converter"
                    root.manager.transition.direction = "left" 
                    
            Button:
                text: "Fractions Converter"
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1, 0, 1
                height: 200
                on_release:
                    app.root.current = "Fractions_converter"
                    root.manager.transition.direction = "left"
                    
            Button:
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1, 0, 1
                height: 200
                text: "Percentages Converter"
                on_release:
                    app.root.current = "Percentages_converter"
                    root.manager.transition.direction = "left"     
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                background_color: 0, 0, 1, 1
                text: "Geometry"
            
            Button:
                text: "Pythagorean Calculator"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 1, 0, 1, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Pythagorean"
                    root.manager.transition.direction = "left"
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                background_color: 0, 0, 1, 1
                text: "Statistics"
            
            Button:
                text: "Statistical Calculator"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 1, 0, 0, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Statistical_Calculator"
                    root.manager.transition.direction = "left"
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                background_color: 0, 0, 1, 1
                text: "Other"
                
            Button:
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1.5, 0, 1
                height: 200
                text: "Tip Calculator"
                on_release:
                    app.root.current = "Tip_Calculator"
                    root.manager.transition.direction = "left"         
                    
            Button:
                font_size: '20sp'
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Button:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Visit KSquared-Mathematics"
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.ksquaredmathematics.com/subscribe')
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-Mathematics"
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 800
                width: 800
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-Mathematics?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "KSquared-Mathematics App v0.1"
                
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
                
            
""")


#Basic
Builder.load_string("""
<Basic>
    id:Basic
    name:"Basic"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Basic Calculator"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        Base_entry.text = ""
                        list_of_steps.clear_widgets()       
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
        
                TextInput:
                    id: Base_entry
                    text: Base_entry.text
                    hint_text: "Entry:"
                    multiline: False
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Basic.steps(Base_entry.text)    
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Basic(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Basic, self).__init__(**kwargs)
            
    layouts = []
    def steps(self,entry):
        print()
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            print("entry",entry)
            self.ids.list_of_steps.add_widget(Label(text="Expression entered : " + entry, font_size = '15sp', size_hint_y= None, height=100))
            
            Answer = str(eval(str(entry).replace("^","**")))
            Answer = "{:,}".format(float(Answer.replace(",","")))
            print("Answer",Answer)
            
            self.ids.list_of_steps.add_widget(Label(text="Answer: " + '[color=33CAFF]' + Answer + '[/color]', markup=True, font_size = '15sp', size_hint_y= None, height=100))
        
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Basic Calculator cannot compute" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            


#EXPONENTS STEPS
Builder.load_string("""
<Exponents_steps>
    id:Exponents_steps
    name:"Exponents_steps"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Exponents Solver"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        Power_entry.text = ""
                        Base_entry.text = ""
                        list_of_steps.clear_widgets()       
                        
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Base ^ Power"
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
        
                TextInput:
                    id: Base_entry
                    text: Base_entry.text
                    hint_text: "Base:"
                    multiline: False
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:3 - len(Base_entry.text)]           
            
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5        
        
                TextInput:
                    id: Power_entry
                    text: Power_entry.text
                    hint_text: "Power:"
                    multiline: False
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10              
                    input_filter: lambda text, from_undo: text[:2 - len(Power_entry.text)]           
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Exponents_steps.steps(Base_entry.text + "$" + Power_entry.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Exponents_steps(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Exponents_steps, self).__init__(**kwargs)

    layouts = []
    def steps(self,entry):
        print()
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            print("entry",entry)
            display = entry.replace("$","^")
            entry_list = entry.split("$")
            print("display :" + display)
            self.ids.list_of_steps.add_widget(Label(text="Expression entered : " + display, font_size = '15sp', size_hint_y= None, height=100))
            Answer = str(eval(str(display).replace("^","**")))
            Answer = "{:,}".format(float(Answer.replace(",","")))
            print("Answer",Answer)
            self.ids.list_of_steps.add_widget(Label(text="Answer: " + '[color=33CAFF]' + Answer + '[/color]', markup=True, font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            entry = entry_list
            print("entry split: ",entry)
            print()
            
            base = entry_list[0]
            print("base",base)
            
            power = entry_list[1]
            print("power",power)
            
            if power.find("-") < 0:
                self.ids.list_of_steps.add_widget(Label(text="Proof of work:", font_size = '15sp', size_hint_y= None, height=100))
                
                i = 0
                product = base
                power_ = power
                while i < float(power_):
                    length = '[color=33CAFF]' + product + '[/color]' + " * " + base
                    print("length",length)
                    if int(power) > 1:
                        self.ids.list_of_steps.add_widget(Label(text= length ,font_size = '15sp', markup=True, size_hint_y= None, height=100))
                    else:
                        self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + product + '[/color]', markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    power = int(power) - 1
                    print("power",power)
                    product = "{:,}".format(float(product.replace(",","")) * float(base))
                    print("product",product)
                    i = i + 1
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
                
#Percentage_Calculator
Builder.load_string("""
<Percentage_Calculator>
    id:Percentage_Calculator
    name:"Percentage_Calculator"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Percentage Calculator"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        number.text = ""
                        perc.text = ""
                        list_of_steps.clear_widgets()       
                                                    
            TextInput:
                id: number
                text: number.text
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10
                hint_text: "Number:"
                input_filter: lambda text, from_undo: text[:8 - len(number.text)]           
            
            TextInput:
                id: perc
                text: perc.text
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10         
                hint_text: "Percent:"
                input_filter: lambda text, from_undo: text[:8 - len(perc.text)]           
            
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5   
                    
                Button:
                    id: steps
                    text: "Increase"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Percentage_Calculator.increase(number.text + "&" + perc.text)    
                          
                Button:
                    id: steps
                    text: "Decrease"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Percentage_Calculator.decrease(number.text + "&" + perc.text)
    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Percentage_Calculator(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Percentage_Calculator, self).__init__(**kwargs)
            
    layouts = []
    def increase(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
           print("INC", entry)
           
           number = entry[:entry.find("&")]
           print("Number",number)
           perc = entry[entry.find("&")+1:]
           print("Perc",perc)
           
           amount = str(float(number) * float(perc) / 100)
           print("amount",amount)
           
           increase = str(float(number) + float(amount))
           print("increase",increase)
           
           self.ids.list_of_steps.add_widget(Label(text= perc + "% of " + number + " = " + amount,font_size = '15sp', size_hint_y= None, height=100))
           self.ids.list_of_steps.add_widget(Label(text= number + " + " + amount + " = " + increase,font_size = '15sp', size_hint_y= None, height=100))
           self.layouts.append(layout)
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
                
    def decrease(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
           print("DEC",entry)
           
           number = entry[:entry.find("&")]
           print("Number",number)
           perc = entry[entry.find("&")+1:]
           print("Perc",perc)
           
           amount = str(float(number) * float(perc) / 100)
           print("amount",amount)
           
           decrease = str(float(number) - float(amount))
           print("decrease",decrease)
           
           self.ids.list_of_steps.add_widget(Label(text= perc + "% of " + number + " = " + amount,font_size = '15sp', size_hint_y= None, height=100))
           self.ids.list_of_steps.add_widget(Label(text= number + " - " + amount + " = " + decrease,font_size = '15sp', size_hint_y= None, height=100))
           self.layouts.append(layout)
           
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
                

#PEMDAS
Builder.load_string("""
<PEMDAS>
    id:PEMDAS
    name:"PEMDAS"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "PEMDAS"
                
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
            
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        list_of_steps.clear_widgets() 
            
            TextInput:
                id: entry
                text: entry.text
                hint_text: "Enter expression:"
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    PEMDAS.steps(entry.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class PEMDAS(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(PEMDAS, self).__init__(**kwargs)
                
    layouts = []
    def steps(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("entry",entry)
        
        
        try:
            #Parentheses
            a = entry
            a = a.strip()
            a = a.replace(" ","").replace("÷","/").replace("×","*")
            print(a)
            print()
            print("------------------------------")
            print()
            
            a = a.replace(" ","")
            a = a.replace("+-","-")
            a = a.replace("-+","-")
            a = a.replace("+"," + ")
            a = a.replace("-"," - ")
            a = a.replace("**", "^")
            a = a.replace("*"," * ")
            a = a.replace("/"," / ")
            a = a.replace(" ^ - ","^-")
            a = a.replace("^*","^")
            a = a.replace("*(","(")
            a = a.replace("* (","(")
            a = a.replace("(","*(")
            a = a.replace("+ *(","+ (")
            a = a.replace("- *(","- (")
            a = a.replace("^*","^")
            a = a.replace("/ *","/")
            
            
            if a[0] == "*":
                a = a[1:]
                print("a =",a)
            
            
            print("Expression Entered :      ",a)
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            self.ids.list_of_steps.add_widget(Label(text="Expression entered : ", font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= entry, font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            #String Method to look for Parentheses
            if a.count("(") == a.count(")") and a.count("(") > 0 and a.count("(") > 0:
                  i = 0
                  while i < len(a):
                    right_par = a.find(")")
                    left_par = a[:right_par].rfind("(")
                    if right_par and left_par == -1:
                        print("breaking loop, no pars")
                        break
                    range_pars = a[left_par:right_par+1]
                    range_pars = range_pars.replace("^","**")
                    print(range_pars)
                    evaled = eval(range_pars)
                    evaled = str(evaled)
                    print(evaled)
                    range_pars = range_pars.replace("**","^")
                    if a.count("(") and a.count(")") == 0:
                        print("breaking loop, a.count(()) = 0")
                        break
                    print()
                    print()
                    print("Parentheses to Solve :    ",a[:left_par],Back.GREEN,range_pars,Style.RESET_ALL,a[right_par+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Parentheses Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:left_par] + '[color=33CAFF]' + range_pars + '[/color]' + a[right_par+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    replaced = a.replace(range_pars,evaled)
                    print()
                    print("Parentheses Solved :      ",a[:left_par],Back.GREEN,evaled,Style.RESET_ALL,a[right_par+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Parentheses Solved : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:left_par] + '[color=33CAFF]' + evaled + '[/color]' + a[right_par+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    print("replaced to a:",replaced)
                    a = replaced
                    print("a =",a)
                    i = i + 1 
            
            elif a.count("(") == 0 and a.count(")") == 0:
                print("No Parenthesis, continue to exponents step")
                
            else:
                print("Parentheses Unbalanced!")
            
            
            a = a.replace(" ","")
            a = a.replace("+-","-")
            a = a.replace("-+","-")
            a = a.replace("+"," + ")
            a = a.replace("-"," - ")
            a = a.replace("**", "^")
            a = a.replace("*"," * ")
            a = a.replace("/"," / ")
            a = a.replace(" ^ - ","^-")
            a = a.replace("^*","^")
            a = a.replace("* (","(")
            a = a.replace("(","*(")
            a = a.replace("+ *(","+ (")
            a = a.replace("- *(","- (")
            a = a.replace("^*","^")
            a = a.replace("/ *","/")
            
            if a[0] == "*":
                a = a[1:]
                print("a =",a)
            
            #String Method to look for Exponents
            i = 0
            if a.count("^") > 0:
                while i < len(a):
                    carrot = a.find("^")
                    if carrot == -1:
                        break
                    print("carrot at index: ",carrot)
                    exp_right_side = a[carrot:]
                    print("exp_right_side",exp_right_side)
                    exp_right_space = exp_right_side.find(" ")
                    print("exp_right_space",exp_right_space)
                    if exp_right_space == -1:
                        exp_right_space = exp_right_side.rfind("")
                    print("exp_right_space",exp_right_space)
                    exp_right_side = a[carrot:carrot + exp_right_space]
                    print("right_side",exp_right_side)
                    exp_left_space = a[:carrot+1].rfind(" ")
                    print("left_side",exp_left_space)
                    if exp_left_space == -1:
                        exp_left_space = a[:carrot+1].find("")
                        print("left_side",exp_left_space)
                    exponent_range = a[exp_left_space:carrot + exp_right_space+1]
                    print("exp_range",exponent_range)
                    if exponent_range[:] == "-":
                        negative = exponent_range.find("-")
                        print("Negative",negative)
                        carrot_inner = exponent_range.find("^")
                        print("carrot_inner",carrot_inner)
                        exponent_left_range = exponent_range[negative:carrot_inner]
                        print("exponent_left_range",exponent_left_range)
                        exponent_left_sliced = "(" + exponent_left_range + ")"
                        exponent_range = exponent_range.replace(exponent_left_range,exponent_left_sliced)
                        print("exponent",exponent_range)
                    print("Exponent to be solved:",exponent_range)
                    exponent_range = exponent_range.replace("^","**")
                    evaled = str(eval(exponent_range))
                    exponent_range = exponent_range.replace("**","^").replace("(","").replace(")","")
                    replaced = a.replace(exponent_range,evaled)
                    print("replaced to a:",replaced)
                    print()
                    print()
                    
                    print("Exponent to Solve :       ",a[:exp_left_space],Back.GREEN,exponent_range,Style.RESET_ALL,a[carrot + exp_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Exponent Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:exp_left_space] + '[color=33CAFF]' + exponent_range + '[/color]' + a[carrot + exp_right_space+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    print()
                    print("Exponent Sovled :         ",a[:exp_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[carrot+exp_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Exponent Solved : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:exp_left_space] + '[color=33CAFF]' + evaled + '[/color]' + a[carrot+exp_right_space+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            
            #String Method to look for Multiplication
            i = 0
            print(a)
            if a.count("*") > 0:
                while i < len(a):
                    a = a.replace(" * ","*")
                    print("mult",a)
                    found_mult = a.find("*")
                    if found_mult == -1:
                        break
                    print(found_mult)
                    mult_right_side = a[found_mult:]
                    print("mult_right_side",mult_right_side)
                    mult_right_space= mult_right_side.find(" ")
                    if mult_right_space == -1:
                        mult_right_space = mult_right_side.rfind("")
                    print("mult_right_found at index:",mult_right_space)
                    mult_left_side = a[:found_mult]
                    print("mult_left_side",mult_left_side)
                    mult_left_space = mult_left_side.rfind(" ")
                    if mult_left_space == -1:
                        mult_left_space = mult_left_side.find("")
                    print("mult_left_found at index:",mult_left_space)
                    mult_range = a[mult_left_space:found_mult + mult_right_space+1]
                    if mult_range == "":
                        break
                    print("mult_range",mult_range)
                    evaled = eval(mult_range)
                    print(evaled)
                    evaled = str(evaled)
                    evaled = evaled.replace("*"," * ")
                    replaced = a.replace(mult_range,evaled)
                    print("replaced to a:",replaced)
                    
                    if evaled.count("-") == 1:
                        evaled = "(" + evaled + ")"
                    
                    print()
                    print()
                    print("Multiplication to Solve : ",a[:mult_left_space],Back.GREEN,mult_range,Style.RESET_ALL,a[found_mult+mult_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Multiplication Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:mult_left_space] + '[color=33CAFF]' + mult_range + '[/color]' + a[found_mult+mult_right_space+1:],markup=True , font_size = '15sp', size_hint_y= None, height=100))
                    
                    print()
                    print("Multiplication Solved :   ", a[:mult_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_mult+mult_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Multiplication Solved : ", font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:mult_left_space] + '[color=33CAFF]' + evaled + '[/color]'  + a[found_mult+mult_right_space+1:], markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)
   
                i = i + 1
            
            #String Method to look for Division
            i = 0
            print(a)
            if a.count("/") > 0:
                while i < len(a):
                    a = a.replace(" / ","/")
                    print("div",a)
                    found_div = a.find("/")
                    if found_div == -1:
                        break
                    print(found_div)
                    div_right_side = a[found_div:]
                    print("div_right_side",div_right_side)
                    div_right_space= div_right_side.find(" ")
                    if div_right_space == -1:
                        div_right_space = div_right_side.rfind("")
                    print("div_right_found at index:",div_right_space)
                    div_left_side = a[:found_div]
                    print("div_left_side",div_left_side)
                    div_left_space = div_left_side.rfind(" ")
                    if div_left_space == -1:
                        div_left_space = div_left_side.find("")
                    print("div_left_found at index:",div_left_space)
                    div_range = a[div_left_space:found_div + div_right_space+1]
                    if div_range == "":
                        break
                    print("div_range",div_range)
                    evaled = eval(div_range)
                    print(evaled)
                    evaled = str(evaled)
                    evaled = evaled.replace("/"," / ")
                    replaced = a.replace(div_range,evaled)
                    print("replaced to a:",replaced)
                    
                    if evaled.count("-") == 1:
                        evaled = "(" + evaled + ")"

                    print()
                    print()
                    #print("Division to Solve : ",a[:div_left_space],Back.GREEN,div_range,Style.RESET_ALL,a[found_div+div_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Division Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:div_left_space] + '[color=33CAFF]' + div_range + '[/color]' + a[found_div+div_right_space+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    
                    print()
                    #print("Division Solved :   ", a[:div_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_div+div_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Division Solved : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:div_left_space] + '[color=33CAFF]' + evaled + '[/color]' + a[found_div+div_right_space+1:],markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            
            #String Method to look for Addition
            i = 0
            while i < len(a):
                if a.count("+") > 0:
                    a = a.replace(" + ","+")
                    print("add",a)
                    found_add = a.find("+")
                    if found_add == -1:
                        break
                    print('found_add',found_add)
                    add_left = a[:found_add]
                    print('add_left',add_left)
                    add_left_space = add_left.rfind(" ")
                    print('add_left_space',add_left_space)
                    if add_left_space == -1:
                        add_left_space = add_left.find("")
                        print('add_left_space',add_left_space)
                    add_right = a[found_add+1:]
                    print('add_right',add_right)
                    add_right_space = add_right.find(" ")
                    print('add_right_space',add_right_space)
                    if add_right_space == -1:
                        add_right_space = add_right.rfind("")
                        print('add_right_space',add_right_space)
                    add_range = a[add_left_space:found_add+add_right_space+1]
                    if add_range == "":
                        break
                    print('add_range',add_range)
                    evaled = eval(add_range)
                    print('evaled',evaled)
                    evaled = str(evaled)
                    replaced = a.replace(add_range,evaled)
                    print("replaced to a:",replaced)

                    print()
                    print()
                    #print("Addition to Solve :       ",a[:add_left_space],Back.GREEN,add_range,Style.RESET_ALL,a[found_add+add_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Addition Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:add_left_space] + '[color=33CAFF]' + add_range + '[/color]' + a[found_add+add_right_space+1:],markup=True , font_size = '15sp', size_hint_y= None, height=100))
                    
                    print()
                    #print("Addition  Solved :        ",a[:add_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_add+add_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Addition Solved : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:add_left_space] + '[color=33CAFF]' + evaled + '[/color]' + a[found_add+add_right_space+1:],markup=True , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            
            #String Method to look for Subtraction
            i = 0 
            while i < len(a):
                if a.count("-") > 0:
                    a = a.replace(" - ","-")
                    print("sub",a)
                    found_sub = a.find("-")
                    if found_sub == -1:
                        break
                    print("found_sub",found_sub)
                    if found_sub == 0:
                        found_sub = a.rfind("-")
                    sub_left = a[:found_sub]
                    print("sub_left",sub_left)
                    if sub_left == "":
                        break
                    sub_left_space = sub_left.rfind(" ")
                    if sub_left_space == -1:
                        sub_left_space = sub_left.find("")
                        print("sub_left_space",sub_left_space)
                    sub_right = a[found_sub+1:]
                    print('sub_right',sub_right)
                    sub_right_space = sub_right.find(" ")
                    if sub_right_space == -1:
                        sub_right_space = sub_right.rfind("")
                        print("sub_right_space",sub_right_space)
                    sub_range = a[sub_left_space:found_sub+sub_right_space+1]
                    print("sub_range",sub_range)
                    if sub_range == "":
                        break
                    evaled = eval(sub_range)
                    print("evaled",evaled)
                    evaled = str(evaled)
                    replaced = a.replace(sub_range, evaled)
                    print("replaced to a:",replaced)
                    a = replaced
                    print("s",a)
 
                    print()
                    print()
                    #print("Subtraction to Solve :    ",a[:sub_left_space],Back.GREEN,sub_range,Style.RESET_ALL,a[found_sub+sub_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Subtraction Step : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:sub_left_space] + '[color=33CAFF]'  + sub_range + '[/color]' + a[found_sub+sub_right_space+1:],markup=True , font_size = '15sp', size_hint_y= None, height=100))
                    
                    print()
                    #print("Subtraction  Solved :     ",a[:sub_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_sub+sub_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Subtraction Solved : " , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:sub_left_space] + '[color=33CAFF]'  + evaled + '[/color]'  + a[found_sub+sub_right_space+1:],markup=True , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            a = a.replace(" ","")
            a = a.replace("e - ","e-")
            
            #print Answer with commas
            a = float(a)
            a = format(a,",")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("Answer:                     ",a)
            self.ids.list_of_steps.add_widget(Label(text="Final Answer : ", font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= a, font_size = '15sp', size_hint_y= None, height=100))

        except Exception:
            try:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                    
            except Exception:               
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)  
                

# Fractions Calculator
Builder.load_string("""
<Fractions>
    id:Fractions
    name:"Fractions"
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Fraction Steps Calculator"
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        a.text = ""
                        b.text = ""
                        list_of_steps.clear_widgets()            
                    
            Label:
                font_size: '15sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Whole(Numerator/Denomenator)"       
                   
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
        
                TextInput:
                    id: a
                    text: a.text
                    hint_text: "Fraction 1:"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5        
                                                    
                TextInput:
                    id: b
                    text: b.text
                    hint_text:  "Fraction 2:"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5  
    
                Button:
                    id: steps
                    text: "+"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 1, 0, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions.add(a.text + "$" + b.text)  
                
                Button:
                    id: steps
                    text: "-"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions.sub(a.text + "$" + b.text) 
                        
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5  
    
                Button:
                    id: steps
                    text: "x"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 1, 0, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions.mult(a.text + "$" + b.text)  
                
                Button:
                    id: steps
                    text: "÷"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions.div(a.text + "$" + b.text) 
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

class Fractions(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Fractions, self).__init__(**kwargs)

    layouts = []
    def add(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print("entry",entry)
            answer = ""
            #Fraction and Fraction
            if entry.count("/") == 2 and entry.count("(") == 0 and entry.count(")") == 0:
                print("ADD F + F")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                if entry_list[0].count("/") == 1:
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][:frac_sign_index]
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                if entry_list[1].count("/") == 1:
                    frac_sign_index = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_index]
                    denom_b = entry_list[1][frac_sign_index+1:]
                    print("denom_b",denom_b)
                lcm = str(np.lcm(int(denom_a),int(denom_b)))
                print("lcm",lcm)
                self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                if int(denom_a) != int(denom_b):
                    print()
                    diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + entry_list[0] + "(" + diff_a + ")" + " + " + "(" + diff_b + ")" + entry_list[1] + "(" + diff_b + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " + " + str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    numer_added = str(int(diff_a) * int(numer_a) + int(diff_b) * int(numer_b))
                    answer = numer_added + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                    numer_added = str(int(numer_b) + int(numer_a)).replace(".0","")
                    answer = numer_added + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                
            #Fraction and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 1 and entry.count(")") == 1:
                print("ADD F & WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF + F")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_one = entry_list[0][:left_par]
                    print("whole_one",whole_one)
                    frac_sign_index = entry_list[0].find("/")
                    denom_a_pre = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a_pre",denom_a_pre)
                    numer_a_pre = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a_pre",numer_a_pre)
                    wf = str(int(whole_one) * int(denom_a_pre) + int(numer_a_pre)).replace(".0","") + "/" + str(denom_a_pre)
                    print("wf",wf)
                    frac_sign_index = wf.find("/")
                    denom_a = wf[frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = wf[:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    frac = entry_list[1]
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:]
                    
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + wf ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= wf + " + " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + wf + "(" + diff_a + ")" + " + " + "(" + diff_b + ")" + entry_list[1] + "(" + diff_b + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " + " + str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))                        
                        numer_add = str(int(diff_a) * int(numer_a) + int(diff_b) * int(numer_b))
                        answer = numer_add + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_added = str(int(numer_a) + int(numer_b)).replace(".0","")
                        answer = numer_added + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                # If the second frac is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole_two = entry_list[1][:left_par]
                    print("whole_two",whole_two)
                    frac_sign_index = entry_list[1].find("/")
                    denom_b_pre = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b_pre",denom_b_pre)
                    numer_b_pre = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b_pre",numer_b_pre)
                    wf = str(int(whole_two) * int(denom_b_pre) + int(numer_b_pre)).replace(".0","") + "/" + str(denom_b_pre)
                    print("wf",wf)
                    frac_sign_index = wf.find("/")
                    denom_b = wf[frac_sign_index+1:]
                    print("denom_b",denom_b)
                    numer_b = wf[:frac_sign_index]
                    print("numer_b",numer_b)
                    
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[0].find("/")
                    numer_a = entry_list[0][:frac_sign_two]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_two+1:]
                    print("denom_a",denom_a)
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + wf ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " + " + wf ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + entry_list[0] + "(" + diff_a + ")" + " + " + "(" + diff_b + ")" + wf + "(" + diff_b + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " + " + str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))                        
                        numer_add = str(int(diff_a) * int(numer_a) + int(diff_b) * int(numer_b))
                        answer = numer_add + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_added = str(int(numer_a) + int(numer_b)).replace(".0","")
                        answer = numer_added + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
            #Fraction and Whole    
            if entry.count("/") == 1 and entry.count("(") == 0 and entry.count(")") == 0:
                print("ADD F + W")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the F
                if entry_list[0].count("(") == 0 and entry_list[0].count(")") == 0 and entry_list[0].count("/") == 1:
                    print("F + W")
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][:frac_sign_index]
                    print("numer_a",numer_a)
                    lcm = denom_a
                    print("lcm",lcm)
                    whole_frac_numer = str(int(entry_list[1]) * int(lcm))
                    whole_frac = str(int(entry_list[1]) * int(lcm)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + whole_frac,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " + " + whole_frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(whole_frac_numer) + int(numer_a)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the F
                if entry_list[1].count("(") == 0 and entry_list[1].count(")") == 0 and entry_list[1].count("/") == 1:
                    print("w + F")
                    frac_sign_index = entry_list[1].find("/")
                    denom_a = entry_list[1][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[1][:frac_sign_index]
                    print("numer_a",numer_a)
                    lcm = denom_a
                    print("lcm",lcm)
                    whole_frac_numer = str(int(entry_list[0]) * int(lcm))
                    whole_frac = str(int(entry_list[0]) * int(lcm)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + whole_frac,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " + " + entry_list[1] + " = "  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(whole_frac_numer) + int(numer_a)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole and Whole(Fraction)
            if entry.count("/") == 1 and entry.count("(") == 1 and entry.count(")") == 1:
                print("ADD W , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF + W")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole = entry_list[0][:left_par]
                    print("whole",whole)
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac = str(int(whole) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:]
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[1]) * int(lcm))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(lcm)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    frac_denom = frac[frac_div_sign+1:]
                    lcm_diff = str(int(lcm) / int(frac_denom)).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text= "(" + lcm_diff + ")" + frac + "(" + lcm_diff + ")" + " + " + whole_frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(int(lcm_diff) * int(frac_numer)) + "/"  + str(int(lcm_diff) * int(frac_denom)) + " + " + whole_frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    frac_numer = str(int(lcm_diff) * int(frac_numer))
                    answer = str(int(whole_numer) + int(frac_numer)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    
                # If the second is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("W + WF")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole = entry_list[1][:left_par]
                    print("whole",whole)
                    frac_sign_index = entry_list[1].find("/")
                    numer_a = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac = str(int(whole) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    print("frac",frac)                    
                    frac_sign_two = entry_list[0].find("/")
                    numer_b = entry_list[0][:frac_sign_two]
                    denom_b = entry_list[0][frac_sign_two+1:]
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " + " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[0]) * int(lcm))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(lcm)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    frac_denom = frac[frac_div_sign+1:]
                    lcm_diff = str(int(lcm) / int(frac_denom)).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " + " + "(" + lcm_diff + ")" + frac + "(" + lcm_diff + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text=   whole_frac + " + " + str(int(lcm_diff) * int(frac_numer)) + "/" + str(int(lcm_diff) * int(frac_denom))  + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    frac_numer = str(int(lcm_diff) * int(frac_numer))
                    answer = str(int(whole_numer) + int(frac_numer)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole(Fraction) and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 2 and entry.count(")") == 2:
                print("ADD WF , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF + WF")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_a = entry_list[0][:left_par]
                    print("whole_a",whole_a)
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac_a = str(int(whole_a) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    frac_a_sign = frac_a.find("/")
                    frac_numer_a = frac_a[:frac_a_sign]
                    
                    frac_sign_two = entry_list[1].find("/")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    numer_b = entry_list[1][left_par+1:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:right_par]
                    whole_b = entry_list[1][:left_par]
                    frac_b = str(int(whole_b) * int(denom_b) + int(numer_b)).replace(".0","") + "/" + str(denom_b)
                    frac_b_sign = frac_b.find("/")
                    frac_numer_b = frac_b[:frac_b_sign]
                    
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac_a ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac_a + " + " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + frac_a + "(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + " + " + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")" +frac_b + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    lcm_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    lcm_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    numer_conv_a = str(int(frac_numer_a) * int(lcm_a)).replace(".0","")
                    numer_conv_b = str(int(frac_numer_b) * int(lcm_b)).replace(".0","")
                    answer = str(int(numer_conv_a) + int(numer_conv_b)) + "/" + str(lcm)
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= numer_conv_a + "/" + str(lcm) + " + " + numer_conv_b + "/" + str(lcm),font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            sol = ""        
            #Whole and Whole   
            if entry.count("/") == 0 and entry.count("(") == 0 and entry.count(")") == 0:
                print("ADD W , W")
                entry = entry.replace("$"," + ")
                print("entry",entry)
                sol = str(eval(str(entry)))
                print("sol",sol)
                self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry + " = ",font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= sol ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
 
            #FRACTION ANSWER REDUCER               
            print("trying to reduce")    
            if answer != "" and sol == "":
                numer_sol_list = str(answer).split("/")
                print("numer_sol_list",numer_sol_list)
                if int(numer_sol_list[0]) > int(numer_sol_list[1]):
                    denom_sol = int(numer_sol_list[1])
                    numer_sol = int(numer_sol_list[0])
                    diff = numer_sol / denom_sol
                    print("diff",diff)
                    dec_index = str(diff).find(".")
                    print("dec_index",dec_index)
                    diff = str(diff)[:dec_index]
                    print("diff",diff)
                    remainder = str(numer_sol % denom_sol)
                    print("remainder ",remainder)
                    
                    if int(numer_sol_list[0]) % int(numer_sol_list[1]) == 0 and int(remainder) == 0:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        if int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                            while int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 2
                                print("remainder reduced further 2: ",remainder)
                                denom_sol = int(denom_sol) / 2
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 3
                                print("remainder reduced further 3: ",remainder)
                                denom_sol = int(denom_sol) / 3
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 5
                                print("remainder reduced further 5: ",remainder)
                                denom_sol = int(denom_sol) / 5
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        
                elif int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 2")
                    while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 2
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 2
                        print("numer_sol_list[1]",numer_sol_list[1])
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 3")
                    while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 3
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 3
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 5")
                    while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 5
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 5
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                elif int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                   answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                   self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+answer  ,font_size = '15sp', size_hint_y= None, height=100))
                   self.layouts.append(layout)  
                
                elif int(numer_sol_list[0]) == 0:
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)  
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input " ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)

    def sub(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print("entry",entry)
            answer = ""
            #Fraction and Fraction
            if entry.count("/") == 2 and entry.count("(") == 0 and entry.count(")") == 0:
                print("SUB F - F")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                if entry_list[0].count("/") == 1:
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][:frac_sign_index]
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                if entry_list[1].count("/") == 1:
                    frac_sign_index = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_index]
                    denom_b = entry_list[1][frac_sign_index+1:]
                    print("denom_b",denom_b)
                lcm = str(np.lcm(int(denom_a),int(denom_b)))
                print("lcm",lcm)
                self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                if int(denom_a) != int(denom_b):
                    print()
                    diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + entry_list[0] + "(" + diff_a + ")" + " - " + "(" + diff_b + ")" + entry_list[1] + "(" + diff_b + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " - " + str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    numer_sub = str(int(diff_a) * int(numer_a) - int(diff_b) * int(numer_b))
                    answer = numer_sub + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                    numer_sub = str(int(numer_a) - int(numer_b)).replace(".0","")
                    answer = numer_sub + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                
            #Fraction and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 1 and entry.count(")") == 1:
                print("SUB F - WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF - F")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_one = entry_list[0][:left_par]
                    print("whole_one",whole_one)
                    frac_sign_index = entry_list[0].find("/")
                    denom_a_pre = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a_pre",denom_a_pre)
                    numer_a_pre = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a_pre",numer_a_pre)
                    frac = str(int(whole_one) * int(denom_a_pre) + int(numer_a_pre)).replace(".0","") + "/" + str(denom_a_pre)
                    frac_sign_index = frac.find("/")
                    denom_a = frac[frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = frac[:frac_sign_index]
                    print("numer_a",numer_a)
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:]
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + frac + "(" + diff_a + ")" + " - " + "(" + diff_b + ")" + entry_list[1] + "(" + diff_b + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " - " + str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        numer_sub = str(int(diff_a) * int(numer_a) - int(diff_b) * int(numer_b))
                        answer = numer_sub + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_sub = str(int(numer_a) - int(numer_b)).replace(".0","")
                        print("numer_sub",numer_sub)
                        answer = numer_sub + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                # If the second frac is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("F - WF")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole_two = entry_list[1][:left_par]
                    print("whole_two",whole_two)
                    frac_sign_index = entry_list[1].find("/")
                    denom_b_pre = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b_pre",denom_b_pre)
                    numer_b_pre = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b_pre",numer_b_pre)
                    frac = str(int(whole_two) * int(denom_b_pre) + int(numer_b_pre)).replace(".0","") + "/" + str(denom_b_pre)
                    print("frac",frac)
                    frac_sign_two = frac.find("/")
                    numer_a = frac[:frac_sign_two]
                    print("numer_a",numer_a)
                    denom_a = frac[frac_sign_two+1:]
                    print("denom_a",denom_a)
                    
                    frac_sign_two = entry_list[0].find("/")
                    numer_b = entry_list[0][:frac_sign_two]
                    denom_b = entry_list[0][frac_sign_two+1:]
                    
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text=  entry_list[0] + " - "  + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        self.ids.list_of_steps.add_widget(Label(text= "(" + diff_b + ")" + entry_list[0] + "(" + diff_b + ")" + " - " + "(" + diff_a + ")" + frac + "(" + diff_a + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " - " + str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        numer_sub = str(int(diff_b) * int(numer_b) - int(diff_a) * int(numer_a))
                        answer = numer_sub + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_sub = str(int(numer_b) - int(numer_a)).replace(".0","")
                        answer = numer_sub + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
            #Fraction and Whole    
            if entry.count("/") == 1 and entry.count("(") == 0 and entry.count(")") == 0:
                print("SUB F - W")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the F
                if entry_list[0].count("(") == 0 and entry_list[0].count(")") == 0 and entry_list[0].count("/") == 1:
                    print("F - W")
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][:frac_sign_index]
                    print("numer_a",numer_a)
                    lcm = denom_a
                    print("lcm",lcm)
                    whole_frac_numer = str(int(entry_list[1]) * int(lcm))
                    whole_frac = str(int(entry_list[1]) * int(lcm)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + whole_frac,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " - " + whole_frac,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(numer_a) - int(whole_frac_numer)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the F
                if entry_list[1].count("(") == 0 and entry_list[1].count(")") == 0 and entry_list[1].count("/") == 1:
                    print("W - F")
                    frac_sign_index = entry_list[1].find("/")
                    denom_a = entry_list[1][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[1][:frac_sign_index]
                    print("numer_a",numer_a)
                    lcm = denom_a
                    print("lcm",lcm)
                    whole_frac_numer = str(int(entry_list[0]) * int(lcm))
                    whole_frac = str(int(entry_list[0]) * int(lcm)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + whole_frac,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " - " + entry_list[1]  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(whole_frac_numer) - int(numer_a)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole and Whole(Fraction)
            if entry.count("/") == 1 and entry.count("(") == 1 and entry.count(")") == 1:
                print("SUB W , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF - W")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole = entry_list[0][:left_par]
                    print("whole",whole)
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac = str(int(whole) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:]

                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " - " + entry_list[1] + " = " ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[1]) * int(denom_a))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(denom_a)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    self.ids.list_of_steps.add_widget(Label(text= frac + " - " + whole_frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    
                    answer = str(int(frac_numer) - int(whole_numer)) + "/" + str(denom_a)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("W - WF")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole = entry_list[1][:left_par]
                    print("whole",whole)
                    frac_sign_index = entry_list[1].find("/")
                    numer_a = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac = str(int(whole) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    print("frac",frac)                    
                    frac_sign_two = entry_list[0].find("/")
                    numer_b = entry_list[0][:frac_sign_two]
                    denom_b = entry_list[0][frac_sign_two+1:]

                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " - " + frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[0]) * int(denom_a))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(denom_a)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " - " + frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    
                    answer = str(int(whole_numer) - int(frac_numer)) + "/" + str(denom_a)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole(Fraction) and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 2 and entry.count(")") == 2:
                print("Sub WF , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF - WF")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_a = entry_list[0][:left_par]
                    print("whole_a",whole_a)
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac_a = str(int(whole_a) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    frac_a_sign = frac_a.find("/")
                    frac_numer_a = frac_a[:frac_a_sign]
                    
                    frac_sign_two = entry_list[1].find("/")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    numer_b = entry_list[1][left_par+1:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:right_par]
                    whole_b = entry_list[1][:left_par]
                    frac_b = str(int(whole_b) * int(denom_b) + int(numer_b)).replace(".0","") + "/" + str(denom_b)
                    frac_b_sign = frac_b.find("/")
                    frac_numer_b = frac_b[:frac_b_sign]
                    
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac_a ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac_a + " - " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + frac_a + "(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + " - " + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")" +frac_b + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    lcm_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    lcm_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    numer_conv_a = str(int(frac_numer_a) * int(lcm_a)).replace(".0","")
                    numer_conv_b = str(int(frac_numer_b) * int(lcm_b)).replace(".0","")
                    answer = str(int(numer_conv_a) - int(numer_conv_b)) + "/" + str(lcm)
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= numer_conv_a + "/" + str(lcm) + " - " + numer_conv_b + "/" + str(lcm) + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            sol = ""        
            #Whole and Whole   
            if entry.count("/") == 0 and entry.count("(") == 0 and entry.count(")") == 0:
                print("SUB W , W")
                entry = entry.replace("$"," - ")
                print("entry",entry)
                sol = str(eval(str(entry)))
                print("sol",sol)
                self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry + " = ",font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= sol ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
 
            #FRACTION ANSWER REDUCER   
            print("trying to reduce")    
            if answer != "" and sol == "":
                numer_sol_list = str(answer).split("/")
                print("numer_sol_list",numer_sol_list)
                if int(numer_sol_list[0]) > int(numer_sol_list[1]):
                    denom_sol = int(numer_sol_list[1])
                    numer_sol = int(numer_sol_list[0])
                    diff = numer_sol / denom_sol
                    print("diff",diff)
                    dec_index = str(diff).find(".")
                    print("dec_index",dec_index)
                    diff = str(diff)[:dec_index]
                    print("diff",diff)
                    remainder = str(numer_sol % denom_sol)
                    print("remainder ",remainder)
                    if int(numer_sol_list[0]) % int(numer_sol_list[1]) == 0 and int(remainder) == 0:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        if int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                            remainder = int(remainder) / 2
                            print("remainder reduced further",remainder)
                            denom_sol = int(denom_sol) / 2
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        elif int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                            remainder = int(remainder) / 3
                            print("remainder reduced further",remainder)
                            denom_sol = int(denom_sol) / 3
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        elif int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                            remainder = int(remainder) / 5
                            print("remainder reduced further",remainder)
                            denom_sol = int(denom_sol) / 5
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                            self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder) + "/" + str(denom_sol) + ")",font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        if int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0:
                            while int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0:
                                remainder = int(remainder) / 2
                                print("remainder reduced further 2:",remainder)
                                denom_sol = int(denom_sol) / 2
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0:
                            while int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0:
                                remainder = int(remainder) / 3
                                print("remainder reduced further",remainder)
                                denom_sol = int(denom_sol) / 3
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0:
                            while int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0:
                                remainder = int(remainder) / 5
                                print("remainder reduced further",remainder)
                                denom_sol = int(denom_sol) / 5
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        
                elif int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 2")
                    while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 2
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 2
                        print("numer_sol_list[1]",numer_sol_list[1])
                    
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 3")
                    while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 3
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 3
                        print("numer_sol_list[1]",numer_sol_list[1])
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 5")
                    while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 5
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 5
                        print("numer_sol_list[1]",numer_sol_list[1])

                elif int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ answer  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                
                elif int(numer_sol_list[0]) == 0:
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)  
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)

    def mult(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print("entry",entry)
            answer = ""
            #Fraction and Fraction
            if entry.count("/") == 2 and entry.count("(") == 0 and entry.count(")") == 0:
                print("Mult F * F")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                if entry_list[0].count("/") == 1:
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][:frac_sign_index]
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                if entry_list[1].count("/") == 1:
                    frac_sign_index = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_index]
                    denom_b = entry_list[1][frac_sign_index+1:]
                    print("denom_b",denom_b)
                    
                Numerators = numer_a + " x " + numer_b
                Denomenators = denom_a + " x " + denom_b
                N_sol = str(int(numer_a) * int(numer_b))
                D_sol = str(int(denom_a) * int(denom_b))
                self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                Numerators = str(int(numer_a) * int(numer_b))
                Denomenators = str(int(denom_a) * int(denom_b))
                answer = Numerators + "/" + Denomenators
                self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)     
                
            #Fraction and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 1 and entry.count(")") == 1:
                print("Mult F * WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF * F")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_one = entry_list[0][:left_par]
                    print("whole_one",whole_one)
                    frac_sign_index = entry_list[0].find("/")
                    denom_a_pre = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a_pre",denom_a_pre)
                    numer_a_pre = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a_pre",numer_a_pre)
                    frac = str(int(whole_one) * int(denom_a_pre) + int(numer_a_pre)).replace(".0","") + "/" + str(denom_a_pre)
                    frac_sign_index = frac.find("/")
                    denom_a = frac[frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = frac[:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    print("numer_b",numer_b)
                    denom_b = entry_list[1][frac_sign_two+1:]
                    print("denom_b",denom_b)
                    
                    Numerators = str(numer_a + " x " + numer_b)
                    N_sol = str(int(numer_a) * int(numer_b))
                    Denomenators = str(denom_a + " x " + denom_b)
                    D_sol = str(int(denom_a) * int(denom_b))

                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol + "/" + D_sol)
                    
                    self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second frac is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("F * WF")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole_two = entry_list[1][:left_par]
                    print("whole_two",whole_two)
                    frac_sign_index = entry_list[1].find("/")
                    denom_b_pre = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b_pre",denom_b_pre)
                    numer_b_pre = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b_pre",numer_b_pre)
                    frac = str(int(whole_two) * int(denom_b_pre) + int(numer_b_pre)).replace(".0","") + "/" + str(denom_b_pre)
                    print("frac",frac)
                    frac_sign_two = frac.find("/")
                    numer_a = frac[:frac_sign_two]
                    print("numer_a",numer_a)
                    denom_a = frac[frac_sign_two+1:]
                    print("denom_a",denom_a)
                    
                    frac_sign_two = entry_list[0].find("/")
                    numer_b = entry_list[0][:frac_sign_two]
                    denom_b = entry_list[0][frac_sign_two+1:]
                    
                    Numerators = str(numer_a + " x " + numer_b)
                    N_sol = str(int(numer_a) * int(numer_b))
                    Denomenators = str(denom_a + " x " + denom_b)
                    D_sol = str(int(denom_a) * int(denom_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text=  entry_list[0] + " x "  + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol + "/" + D_sol)
                    
                    self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                        
            #Fraction and Whole    
            if entry.count("/") == 1 and entry.count("(") == 0 and entry.count(")") == 0:
                print("MULT F * W")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the F
                if entry_list[0].count("(") == 0 and entry_list[0].count(")") == 0 and entry_list[0].count("/") == 1:
                    print("F * W")
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][:frac_sign_index]
                    print("numer_a",numer_a)

                    Numerators = str(numer_a + " x " + entry_list[1])
                    Denomenators = str(denom_a + " x " + str(1))
                    Numerators_sol = str(int(numer_a) * int(entry_list[1]))
                    Denomenators_sol = str(int(denom_a) * int(1))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " x " + entry_list[1]+ "/1" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(numer_a) * int(entry_list[1])) + "/" + str(int(denom_a) * int(1))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the F
                if entry_list[1].count("(") == 0 and entry_list[1].count(")") == 0 and entry_list[1].count("/") == 1:
                    print("W * F")
                    frac_sign_index = entry_list[1].find("/")
                    denom_a = entry_list[1][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[1][:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    Numerators = str(entry_list[0] + " x " + numer_a)
                    Denomenators = str(denom_a + " x " + str(1))
                    Numerators_sol = str(int(numer_a) * int(entry_list[0]))
                    Denomenators_sol = str(int(denom_a) * int(1))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + "/1" + " x " + entry_list[1] + " = " ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators +" = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer =  str(int(numer_a) * int(entry_list[0])) + "/" + str(int(1) * int(denom_a))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole and Whole(Fraction)
            if entry.count("/") == 1 and entry.count("(") == 1 and entry.count(")") == 1:
                print("MULT W , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF * W")
                    frac_sign_index = entry_list[0].find("/")
                    right_par = entry_list[0].find(")")
                    left_par = entry_list[0].find("(")
                    whole_a = entry_list[0][:left_par]
                    print("whole_a",whole_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    wf = str(int(whole_a) * int(denom_a) + int(numer_a)) + "/" + str(denom_a)
                    wf_numer = str(int(whole_a) * int(denom_a) + int(numer_a))
                    
                    Numerators = str(wf_numer + " x " + entry_list[1])
                    Denomenators = str(denom_a + " x " + str(1))
                    Numerators_sol = str(int(wf_numer) * int(entry_list[1]))
                    Denomenators_sol = str(int(denom_a) * int(1))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + wf,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= wf + " x " + entry_list[1] + "/1" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(wf_numer) * int(entry_list[1])) + "/" + str(int(denom_a) * int(1))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1 and entry_list[1].count("/") == 1:
                    print("W * WF")
                    frac_sign_index = entry_list[1].find("/")
                    right_par = entry_list[1].find(")")
                    left_par = entry_list[1].find("(")
                    whole_a = entry_list[1][:left_par]
                    print("whole_a",whole_a)
                    denom_a = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    numer_a = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    wf = str(int(whole_a) * int(denom_a) + int(numer_a)) + "/" + str(denom_a)
                    wf_numer = str(int(whole_a) * int(denom_a) + int(numer_a))
                    
                    Numerators = str(entry_list[0] + " x " + wf_numer)
                    Denomenators = str(denom_a + " x " + str(1))
                    Numerators_sol = str(int(wf_numer) * int(entry_list[0]))
                    Denomenators_sol = str(int(denom_a) * int(1))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + wf,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " x " + wf + " = " ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators +" = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer =  str(int(wf_numer) * int(entry_list[0])) + "/" + str(int(1) * int(denom_a))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole(Fraction) and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 2 and entry.count(")") == 2:
                print("MULT WF , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1 and entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("WF * WF")
                    
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_a = entry_list[0][:left_par]
                    print("whole_a",whole_a)
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac_a = str(int(whole_a) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    frac_a_sign = frac_a.find("/")
                    frac_numer_a = frac_a[:frac_a_sign]
                    
                    frac_sign_two = entry_list[1].find("/")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    numer_b = entry_list[1][left_par+1:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:right_par]
                    whole_b = entry_list[1][:left_par]
                    frac_b = str(int(whole_b) * int(denom_b) + int(numer_b)).replace(".0","") + "/" + str(denom_b)
                    frac_b_sign = frac_b.find("/")
                    frac_numer_b = frac_b[:frac_b_sign]
                    
                    Numerator = str(int(frac_numer_a) * int(frac_numer_b))
                    Denomenator = str(int(denom_a) * int(denom_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac_a ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac_a + " x " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + frac_numer_a + " x " + frac_numer_b + " = " + Numerator,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + denom_a + " x " + denom_b + " = " + Denomenator ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)

                    answer = str(Numerator + "/" + Denomenator)
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            sol = ""        
            #Whole and Whole   
            if entry.count("/") == 0 and entry.count("(") == 0 and entry.count(")") == 0:
                print("Mult W , W")
                entry = entry.replace("$"," * ")
                print("entry",entry)
                sol = str(eval(str(entry)))
                print("sol",sol)
                self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry + " = ",font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= sol ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
 
            #FRACTION ANSWER REDUCER               
            print("trying to reduce")    
            if answer != "" and sol == "":
                numer_sol_list = str(answer).split("/")
                print("numer_sol_list",numer_sol_list)
                if int(numer_sol_list[0]) > int(numer_sol_list[1]):
                    denom_sol = int(numer_sol_list[1])
                    numer_sol = int(numer_sol_list[0])
                    diff = numer_sol / denom_sol
                    print("diff",diff)
                    dec_index = str(diff).find(".")
                    print("dec_index",dec_index)
                    diff = str(diff)[:dec_index]
                    print("diff",diff)
                    remainder = str(numer_sol % denom_sol)
                    print("remainder ",remainder)
                    
                    if int(numer_sol_list[0]) % int(numer_sol_list[1]) == 0 and int(remainder) == 0:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        if int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                            while int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 2
                                print("remainder reduced further 2: ",remainder)
                                denom_sol = int(denom_sol) / 2
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 3
                                print("remainder reduced further 3: ",remainder)
                                denom_sol = int(denom_sol) / 3
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 5
                                print("remainder reduced further 5: ",remainder)
                                denom_sol = int(denom_sol) / 5
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        
                elif int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 2")
                    while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 2
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 2
                        print("numer_sol_list[1]",numer_sol_list[1])
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 3")
                    while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 3
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 3
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 5")
                    while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 5
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 5
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                elif int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                   answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                   self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+answer  ,font_size = '15sp', size_hint_y= None, height=100))
                   self.layouts.append(layout)  
                
                elif int(numer_sol_list[0]) == 0:
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout) 
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)

    def div(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print("entry",entry)
            answer = ""
            #Fraction and Fraction
            if entry.count("/") == 2 and entry.count("(") == 0 and entry.count(")") == 0:
                print("Div F / F")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                if entry_list[0].count("/") == 1:
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][:frac_sign_index]
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                if entry_list[1].count("/") == 1:
                    frac_sign_index = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_index]
                    denom_b = entry_list[1][frac_sign_index+1:]
                    print("denom_b",denom_b)
                    
                Reciprocal = str(denom_b+ "/" + numer_b)
                Numerators = numer_a + " x " + denom_b 
                Denomenators = denom_a + " x " + numer_b
                N_sol = str(int(numer_a) * int(denom_b))
                D_sol = str(int(denom_a) * int(numer_b))
                self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + entry_list[1] + " = " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + Reciprocal + " = " ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                Numerators = str(int(numer_a) * int(denom_b))
                Denomenators = str(int(denom_a) * int(numer_b))
                answer = Numerators + "/" + Denomenators
                self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)     
                
            #Fraction and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 1 and entry.count(")") == 1:
                print("Div F / WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF / F")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_one = entry_list[0][:left_par]
                    print("whole_one",whole_one)
                    frac_sign_index = entry_list[0].find("/")
                    denom_a_pre = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a_pre",denom_a_pre)
                    numer_a_pre = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a_pre",numer_a_pre)
                    frac = str(int(whole_one) * int(denom_a_pre) + int(numer_a_pre)).replace(".0","") + "/" + str(denom_a_pre)
                    frac_sign_index = frac.find("/")
                    denom_a = frac[frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = frac[:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    print("numer_b",numer_b)
                    denom_b = entry_list[1][frac_sign_two+1:]
                    print("denom_b",denom_b)
                    
                    Reciprocal = str(denom_b+ "/" + numer_b)
                    Numerators = numer_a + " x " + denom_b 
                    Denomenators = denom_a + " x " + numer_b
                    N_sol = str(int(numer_a) * int(denom_b))
                    D_sol = str(int(denom_a) * int(numer_b))

                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + entry_list[1] + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + frac + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol + "/" + D_sol)
                    
                    self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second frac is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("F / WF")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole_two = entry_list[1][:left_par]
                    print("whole_two",whole_two)
                    frac_sign_index = entry_list[1].find("/")
                    denom_b_pre = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b_pre",denom_b_pre)
                    numer_b_pre = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b_pre",numer_b_pre)
                    frac = str(int(whole_two) * int(denom_b_pre) + int(numer_b_pre)).replace(".0","") + "/" + str(denom_b_pre)
                    print("frac",frac)
                    frac_sign_two = frac.find("/")
                    numer_a = frac[:frac_sign_two]
                    print("numer_a",numer_a)
                    denom_a = frac[frac_sign_two+1:]
                    print("denom_a",denom_a)
                    
                    frac_sign_two = entry_list[0].find("/")
                    numer_b = entry_list[0][:frac_sign_two]
                    denom_b = entry_list[0][frac_sign_two+1:]
                    
                    Reciprocal = str(denom_a + "/" + numer_a)
                    Numerators = numer_b + " x " + denom_a 
                    Denomenators = denom_b + " x " + numer_a
                    N_sol = str(int(numer_b) * int(denom_a))
                    D_sol = str(int(denom_b) * int(numer_a))

                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + frac + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol + "/" + D_sol)
                    
                    self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                        
            #Fraction and Whole    
            if entry.count("/") == 1 and entry.count("(") == 0 and entry.count(")") == 0:
                print("Div F / W")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the F
                if entry_list[0].count("(") == 0 and entry_list[0].count(")") == 0 and entry_list[0].count("/") == 1:
                    print("F / W")
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][:frac_sign_index]
                    print("numer_a",numer_a)

                    numer_b = str(entry_list[1])
                    denom_b = str(1)
                    
                    Reciprocal = str(denom_b + "/" + numer_b)
                    Numerators = numer_a + " x " + denom_b 
                    Denomenators = denom_a + " x " + numer_b
                    N_sol = str(int(numer_a) * int(denom_b))
                    D_sol = str(int(denom_a) * int(numer_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + entry_list[1] + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol) + "/" + str(D_sol)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the F
                if entry_list[1].count("(") == 0 and entry_list[1].count(")") == 0 and entry_list[1].count("/") == 1:
                    print("W / F")
                    frac_sign_index = entry_list[1].find("/")
                    denom_a = entry_list[1][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[1][:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    numer_b = str(entry_list[0])
                    denom_b = str(1)
                    
                    whole_frac = numer_b + "/" + denom_b
                    
                    Reciprocal = str(denom_a + "/" + numer_a)
                    Numerators = numer_b + " x " + denom_a
                    Denomenators = denom_b + " x " + numer_a
                    N_sol = str(int(denom_a) * int(numer_b))
                    D_sol = str(int(numer_a) * int(denom_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + entry_list[1] + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + whole_frac + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol) + "/" + str(D_sol)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole and Whole(Fraction)
            if entry.count("/") == 1 and entry.count("(") == 1 and entry.count(")") == 1:
                print("Div W , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF / W")
                    frac_sign_index = entry_list[0].find("/")
                    right_par = entry_list[0].find(")")
                    left_par = entry_list[0].find("(")
                    whole_a = entry_list[0][:left_par]
                    print("whole_a",whole_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    wf = str(int(whole_a) * int(denom_a) + int(numer_a)) + "/" + str(denom_a)
                    wf_numer = str(int(whole_a) * int(denom_a) + int(numer_a))
                    
                    Reciprocal = str("1/" + entry_list[1])
                    Numerators = str(wf_numer + " x " + str(1))
                    Denomenators = str(denom_a + " x " + entry_list[1])
                    Numerators_sol = str(int(wf_numer) * int(1))
                    Denomenators_sol = str(int(denom_a) * int(entry_list[1]))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + wf,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + entry_list[1] + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + wf + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(Numerators_sol) + "/" + str(Denomenators_sol)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1 and entry_list[1].count("/") == 1:
                    print("W / WF")
                    frac_sign_index = entry_list[1].find("/")
                    right_par = entry_list[1].find(")")
                    left_par = entry_list[1].find("(")
                    whole_b = entry_list[1][:left_par]
                    print("whole_b",whole_b)
                    denom_b = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b",denom_b)
                    numer_b = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b",numer_b)
                    
                    wf = str(int(whole_b) * int(denom_b) + int(numer_b)) + "/" + str(denom_b)
                    wf_numer = str(int(whole_b) * int(denom_b) + int(numer_b))
                    
                    Reciprocal = str(denom_b + "/" + wf_numer)
                    Numerators = str(entry_list[0] + " x " + denom_b)
                    Denomenators = str("1" + " x " + wf_numer)
                    Numerators_sol = str(int(entry_list[0]) * int(wf_numer))
                    Denomenators_sol = str(int(1) * int(denom_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + wf,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + wf + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + "/1" + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(Numerators_sol) + "/" + str(Denomenators_sol)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole(Fraction) and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 2 and entry.count(")") == 2:
                print("Div WF , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1 and entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("WF / WF")
                    
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_a = entry_list[0][:left_par]
                    print("whole_a",whole_a)
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac_a = str(int(whole_a) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    frac_a_sign = frac_a.find("/")
                    frac_numer_a = frac_a[:frac_a_sign]
                    
                    frac_sign_two = entry_list[1].find("/")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    numer_b = entry_list[1][left_par+1:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:right_par]
                    whole_b = entry_list[1][:left_par]
                    frac_b = str(int(whole_b) * int(denom_b) + int(numer_b)).replace(".0","") + "/" + str(denom_b)
                    frac_b_sign = frac_b.find("/")
                    frac_numer_b = frac_b[:frac_b_sign]
                    frac_denom_b = frac_b[frac_b_sign+1:]
                    
                    Reciprocal = str(frac_denom_b + "/" + frac_numer_b)
                    Numerator = str(int(frac_numer_a) * int(frac_denom_b))
                    Denomenator = str(int(denom_a) * int(frac_numer_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac_a ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + frac_b + " = " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + frac_a + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + frac_numer_a + " x " + frac_denom_b + " = " + Numerator,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + denom_a + " x " + frac_numer_b + " = " + Denomenator ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)

                    answer = str(Numerator + "/" + Denomenator)
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            sol = ""        
            #Whole and Whole   
            if entry.count("/") == 0 and entry.count("(") == 0 and entry.count(")") == 0:
                print("Div W , W")
                entry = entry.replace("$"," / ")
                print("entry",entry)
                sol = str(eval(str(entry)))
                print("sol",sol)
                self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry + " = ",font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= sol ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
 
            #FRACTION ANSWER REDUCER               
            print("trying to reduce")    
            if answer != "" and sol == "":
                numer_sol_list = str(answer).split("/")
                print("numer_sol_list",numer_sol_list)
                
                if int(numer_sol_list[1]) == 0:
                    print("Undefined")
                    self.ids.list_of_steps.add_widget(Label(text="Undefined" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                
                elif int(numer_sol_list[0]) > int(numer_sol_list[1]):
                    denom_sol = int(numer_sol_list[1])
                    numer_sol = int(numer_sol_list[0])
                    diff = numer_sol / denom_sol
                    print("diff",diff)
                    dec_index = str(diff).find(".")
                    print("dec_index",dec_index)
                    diff = str(diff)[:dec_index]
                    print("diff",diff)
                    remainder = str(numer_sol % denom_sol)
                    print("remainder ",remainder)
                    
                    if int(numer_sol_list[0]) % int(numer_sol_list[1]) == 0 and int(remainder) == 0:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        if int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                            while int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 2
                                print("remainder reduced further 2: ",remainder)
                                denom_sol = int(denom_sol) / 2
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 3
                                print("remainder reduced further 3: ",remainder)
                                denom_sol = int(denom_sol) / 3
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 5
                                print("remainder reduced further 5: ",remainder)
                                denom_sol = int(denom_sol) / 5
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                                
                elif int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 2")
                    while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 2
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 2
                        print("numer_sol_list[1]",numer_sol_list[1])
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 3")
                    while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 3
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 3
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 5")
                    while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 5
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 5
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                elif int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                   answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                   self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+answer  ,font_size = '15sp', size_hint_y= None, height=100))
                   self.layouts.append(layout)  
                
                elif int(numer_sol_list[0]) == 0:
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)    
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)

#Pythagorean STEPS
Builder.load_string("""
<Pythagorean>
    id:Pythagorean
    name:"Pythagorean"
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Pythagorean Calculator"
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        a.text = ""
                        b.text = ""
                        c.text = ""
                        list_of_steps.clear_widgets()            
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "a\u00B2 + b\u00B2 = c\u00B2"       
                                                        
            TextInput:
                id: a
                text: a.text
                multiline: False
                hint_text: "a ="
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10
                input_filter: lambda text, from_undo: text[:3 - len(a.text)]  
                    
            TextInput:
                id: b
                text: b.text
                multiline: False
                hint_text:"b ="
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10          
                input_filter: lambda text, from_undo: text[:3 - len(b.text)]  
                
            TextInput:
                id: c
                text: c.text
                multiline: False
                hint_text:"c ="
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10          
                input_filter: lambda text, from_undo: text[:3 - len(c.text)]  
                
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Pythagorean.steps(a.text + "," + b.text + "," + c.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                          
                    
""")

class Pythagorean(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Pythagorean, self).__init__(**kwargs)
            
    layouts = []
    def steps(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            entry = str(entry).replace(" ","")
            entry = entry.split(",")
            print("entry",entry)
            
            i = 0
            while i< len(entry):
                if entry[i] == '':
                    print("found empty")
                    entry[i] = "0"
                    print("entry[" + str(i) + "] = " + entry[i])
                i = i + 1
            
            print("entry",entry)
            
            a = entry[0]
            print("a: ",a)
                
            b = entry[1]
            print("b: ",b)
                
            c = entry[2]
            print("c: ",c)
            
            c_squared = str(int(c)**2)
            print("c_squared",c_squared)
            
            # 3 + 4 = 5
            if int(entry[0]) > 0 and int(entry[1]) > 0 and int(entry[2]) > 0:
                print()
                print("Is this entry valid?")
                
                entry_evaled = str(eval(str(int(a)**2) + "+" + str(int(b)**2)))
                print("entry_evaled = ",entry_evaled)
                
                if str(entry_evaled) == str(c_squared):
                    print("entry_evaled = c")
                    self.ids.list_of_steps.add_widget(Label(text= str(a) + "\u00B2"  + " + " + str(b) + "\u00B2" + " = " + str(c) + "\u00B2", font_size = '15sp', size_hint_y= None, height=100))
                    
                    a_squared = str(int(a)**2)
                    b_squared = str(int(b)**2)
                    
                    ab = str(int(a_squared) + int(b_squared))
                    
                    self.ids.list_of_steps.add_widget(Label(text= str(a_squared) + " + " + str(b_squared) + " = " + str(c_squared), font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(ab) + " = " + str(c_squared), font_size = '15sp', size_hint_y= None, height=100))

                else:
                    print("entry_evaled does not = c!!!!!!!")
                    self.ids.list_of_steps.add_widget(Label(text= "Input does not equate to triangle!", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
            
            # 3 + b = 5 OR a + 4 = 5
            elif int(entry[0]) >= 0 or int(entry[1]) >= 0 and int(entry[2]) >= 0:
                
                a_squared = str(int(a)**2)
                b_squared = str(int(b)**2)
                c_squared = str(int(c)**2)
                
                if int(entry[0]) > 0 and int(entry[1]) > 0:
                    print("a and b are valid")
                    print()
                    print("Solve for a!")
                    
                    self.ids.list_of_steps.add_widget(Label(text= str(a) + "\u00B2"  + " + " + str(b) + "\u00B2" + " = c\u00B2", font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(a_squared)  + " + " + str(b_squared) + " = c\u00B2", font_size = '15sp', size_hint_y= None, height=100))

                    a_plus_b = int(a_squared) + int(b_squared)
                    print("a_plus_b = ",a_plus_b)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "c\u00B2" + " = " + str(a_plus_b) , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "\u221a(" + " c\u00B2)" + " = " + "\u221a(" + str(a_plus_b) + ")" , font_size = '15sp', size_hint_y= None, height=100))

                    a_plus_b_root = str(float(a_plus_b)**.5)
                    print("a_plus_b_root = ",a_plus_b_root)

                    if a_plus_b_root[-2] == "." and a_plus_b_root[-1] == "0":
                        self.ids.list_of_steps.add_widget(Label(text= "c = " + format(float(a_plus_b_root),","), font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text= "c = " + "\u221a(" + format(float(a_plus_b),",") + ")", font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                                        
                    if a_plus_b_root == "0.0":
                        self.ids.list_of_steps.add_widget(Label(text= "0.0 cannot form a valid line for triangle" ,font_size = '15sp', size_hint_y= None, height=100))
                    
                elif int(entry[0]) > 0 and int(entry[2]) > 0:
                    print("a and c are valid")
                    print()
                    print("Solve for b!")
                    
                    self.ids.list_of_steps.add_widget(Label(text= str(a) + "\u00B2"  + " + " + "b\u00B2" + " = " + str(c) + "\u00B2", font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "b\u00B2" + " = " + str(c) + "\u00B2" + " - " + str(a) + "\u00B2" , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "b\u00B2" + " = " + str(c_squared) + " - " + str(a_squared) , font_size = '15sp', size_hint_y= None, height=100))
                    
                    c_minus_a = int(c_squared) - int(a_squared)
                    print("c_minus_a = ",c_minus_a)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "b\u00B2" + " = " + str(c_minus_a) , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "\u221a(" + " b\u00B2)" + " = " + "\u221a(" + str(c_minus_a) + ")" , font_size = '15sp', size_hint_y= None, height=100))
                    
                    c_minus_a_root = str(float(c_minus_a)**.5)
                    print("c_minus_a_root = ",c_minus_a_root)

                    if c_minus_a_root[-2] == "." and c_minus_a_root[-1] == "0":
                        self.ids.list_of_steps.add_widget(Label(text= "b = " + format(float(c_minus_a_root),","), font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text= "b = " + "\u221a(" + format(float(c_minus_a),",") + ")", font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                    if c_minus_a_root == "0.0":
                        self.ids.list_of_steps.add_widget(Label(text= "0.0 cannot form a valid line for triangle" ,font_size = '15sp', size_hint_y= None, height=100))
                    
                elif int(entry[1]) > 0 and int(entry[2]) > 0:
                    print("b and c are valid")
                    print()
                    print("Solve for a!")
                    
                    self.ids.list_of_steps.add_widget(Label(text= "a\u00B2"  + " + " + str(b) + "\u00B2" + " = " + str(c) + "\u00B2", font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "a\u00B2" + " = " + str(c) + "\u00B2" + " - " + str(b) + "\u00B2" , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "a\u00B2" + " = " + str(c_squared) + " - " + str(b_squared) , font_size = '15sp', size_hint_y= None, height=100))
                    
                    c_minus_b = int(c_squared) - int(b_squared)
                    print("c_minus_b = ",c_minus_b)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "a\u00B2" + " = " + str(c_minus_b) , font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "\u221a(" + " a\u00B2)" + " = " + "\u221a(" + str(c_minus_b) + ")" , font_size = '15sp', size_hint_y= None, height=100))
                    
                    c_minus_b_root = str(float(c_minus_b)**.5)
                    print("c_minus_b_root = ",c_minus_b_root)

                    if c_minus_b_root[-2] == "." and c_minus_b_root[-1] == "0":
                        self.ids.list_of_steps.add_widget(Label(text= "a = " + format(float(c_minus_b_root),","), font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text= "a = " + "\u221a(" + format(float(c_minus_b),",") + ")", font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
                    if c_minus_b_root == "0.0":
                        self.ids.list_of_steps.add_widget(Label(text= "0.0 cannot form a valid line for triangle" ,font_size = '15sp', size_hint_y= None, height=100))
                    
                
            else:
                print("Invalid length")                
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
        
        if entry[0].count("-") > 0 or entry[1].count("-") > 0 or entry[2].count("-") > 0:
            print("entry neg: ",entry)
            self.ids.list_of_steps.add_widget(Label(text= "Cannot have negative sides of a triangle!" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
#Quadratic
Builder.load_string("""
<Quadratic_Formula_Solver>
    id:Quadratic_Formula_Solver
    name:"Quadratic_Formula_Solver"
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                text: "Quadratic Formula Calculator"
                
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1, 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        a.text = ""
                        b.text = ""
                        c.text = ""
                        list_of_steps.clear_widgets()    
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
            
                Label:
                    height: 200
                    font_size: '15sp'
                    size_hint_y: None
                    padding: 5,5
                    text: "ax\u00B2 + bx + c = 0"
                
                Label:
                    height: 200
                    font_size: '15sp'
                    size_hint_y: None
                    padding: 5,5
                    text:
                        '''      -b \u00B1 \u221A(b\u00B2 - 4ac)
                        x = -----------------------
                        '''      '''                2a'''    
                    
            TextInput:
                id: a
                text: a.text
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                hint_text: "a ="
                height: 200
                padding: 10
                input_filter: lambda text, from_undo: text[:3 - len(a.text)]  
                    
                                                 
            TextInput:
                id: b
                text: b.text
                multiline: False
                hint_text: "b ="
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10          
                input_filter: lambda text, from_undo: text[:3 - len(b.text)]  
                
    
            TextInput:
                id: c
                text: c.text
                multiline: False
                hint_text: "c ="
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10          
                input_filter: lambda text, from_undo: text[:3 - len(c.text)]
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5  
    
                Button:
                    id: steps
                    text: "Calculate"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Quadratic_Formula_Solver.steps(a.text + "," + b.text + "," + c.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

class Quadratic_Formula_Solver(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Quadratic_Formula_Solver, self).__init__(**kwargs)

    layouts = []
    def steps(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            entry_list =  entry.split(",")
            print("entry_list",entry_list)
            a = float(entry_list[0])
            b = float(entry_list[1])
            c = float(entry_list[2])
            
            #Check if ax^2 + bx + c = 0
            square = float(b*b - 4*a*c)
            print("square",square)
            
            if square > 0 :
                
                a = str(entry_list[0])
                b_out = "-" + str(entry_list[1])
                b_out = b_out.replace("--","")
                b = str(entry_list[1])
                c = str(entry_list[2])
                
                
                #POSITIVE
                self.ids.list_of_steps.add_widget(Label(text= "x1" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + \u221A(" + b + "\u00B2 - 4" + "(" + a + ")(" + c + "))" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = '15sp', size_hint_y= None, height=300))
                
                ac = " - " + str(4*float(a)*float(c))
                ac = ac.replace("- -","+ ")
                b = str(float(b)**2)
                
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + \u221A(" + b + ac + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = '15sp', size_hint_y= None, height=300))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + \u221A(" + str(square) + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = '15sp', size_hint_y= None, height=300))
                
                squared = str(square**.5)
                print("squared",squared)
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + " + squared + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = '15sp', size_hint_y= None, height=300))
                
                numer = str(float(b_out) + float(squared))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = '15sp', size_hint_y= None, height=300))
                
                denom = str(2 * float(a))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                     " + denom ,font_size = '15sp', size_hint_y= None, height=300))
                
                answera = str(float(numer) / float(denom))
                print("answera",answera)
                self.ids.list_of_steps.add_widget(Label(text="x1 = " + answera ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = '15sp', size_hint_y= None, height=100))
                
                a = str(entry_list[0])
                b_out = "-" + str(entry_list[1])
                b_out = b_out.replace("--","")
                b = str(entry_list[1])
                c = str(entry_list[2])
                
                #NEGATIVE
                self.ids.list_of_steps.add_widget(Label(text= "x2" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - \u221A(" + b + "\u00B2 - 4" + "(" + a + ")(" + c + "))" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = '15sp', size_hint_y= None, height=300))
                
                ac = " - " + str(4*float(a)*float(c))
                ac = ac.replace("- -","+ ")
                b = str(float(b)**2)
                
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - \u221A(" + b +  ac + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = '15sp', size_hint_y= None, height=300))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - \u221A(" + str(square) + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = '15sp', size_hint_y= None, height=300))
                
                squared = str(square**.5)
                print("squared",squared)
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - " + squared + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = '15sp', size_hint_y= None, height=300))
                
                numer = str(float(b_out) - float(squared))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = '15sp', size_hint_y= None, height=300))
                
                denom = str(2 * float(a))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                     " + denom ,font_size = '15sp', size_hint_y= None, height=300))
                
                answerb = str(float(numer) / float(denom))
                print("answerb",answerb)
                self.ids.list_of_steps.add_widget(Label(text="x1 = " + answerb ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="FINAL ANSWER ",font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="x1 = " + answera,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="x2 = " + answerb,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Square Root" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
            
                            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
       	 

Builder.load_string("""
<Percentages_converter>
    id: Percentages_converter
    name:"Percentages_converter"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                text: "Percentages Converter"   
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    text: "Back"
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()  
                        input.text = ""
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: input
                    text: input.text
                    hint_text: "Percentage:"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:4 - len(input.text)] 
                    
            Label:
                size_hint_y: None
                height: 200
                text: "Convert To:"
                font_size: '20sp'
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                         
                Button:
                    text: "Fraction"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        list_of_steps.clear_widgets() 
                        Percentages_converter.convert_perc_to_frac(input.text)
                        
                Button:
                    id: steps
                    text: "Decimal"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Percentages_converter.convert_perc_to_dec(input.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
""")

Builder.load_string("""
<Fractions_converter>
    id: Fractions_converter
    name:"Fractions_converter"
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                text: "Fractions Converter"   
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    text: "Back"
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()  
                        Whole.text = ""
                        Numerator.text = ""
                        Denomenator.text = ""
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: Whole
                    text: Whole.text
                    hint_text: "Whole:"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(Whole.text)] 
            
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: Numerator
                    text: Numerator.text
                    hint_text: "Numerator"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(Numerator.text)] 
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: Denomenator
                    text: Denomenator.text
                    hint_text: "Denomenator"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(Denomenator.text)] 
                    
            Label:
                size_hint_y: None
                height: 200
                text: "Convert To:"
                font_size: '20sp'
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                         
                Button:
                    text: "Percent"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions_converter.convert_frac_to_perc(Whole.text + "(" + Numerator.text + "/" + Denomenator.text + ")")
                        
                Button:
                    id: steps
                    text: "Decimal"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions_converter.convert_frac_to_dec(Whole.text + "(" + Numerator.text + "/" + Denomenator.text + ")")
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height            
    
""")

Builder.load_string("""
<Decimals_converter>
    id: Decimals_converter
    name:"Decimals_converter"
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                text: "Decimals Converter"   
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    text: "Back"
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()  
                        input.text = ""
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: input
                    text: input.text
                    hint_text: "Decimal:"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(input.text)] 
                    
            Label:
                size_hint_y: None
                height: 200
                text: "Convert To:"
                font_size: '20sp'
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                         
                Button:
                    text: "Fraction"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        list_of_steps.clear_widgets() 
                        Decimals_converter.convert_dec_to_frac(input.text)
                        
                Button:
                    id: steps
                    text: "Percent"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Decimals_converter.convert_dec_to_perc(input.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height            
    
""")

class Decimals_converter(Screen):
    def __init__(self, **kwargs):
        super(Decimals_converter, self).__init__(**kwargs)
            
    layouts = []
    def convert_dec_to_frac(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            if entry.count(".") == 1:
                decimal_index = entry.find(".")
                print("decimal_index",decimal_index)
                whole = str(entry[:decimal_index])
                print("whole",whole)
                if whole == "0":
                    whole = ""
                print("whole",whole)
                dec_for_frac = entry[decimal_index+1:]
                print("dec_for_frac",dec_for_frac)
                if len(dec_for_frac) == 1:
                    dec_for_frac = dec_for_frac + "0"
                numerator = dec_for_frac
                print("numerator = ",numerator)
                
                denomenator = "1" + "0" * len(numerator)
                print("denomenator = ",denomenator)
                
                numerator = int(numerator)
                print("numerator = ",numerator)
                
                if int(numerator) % 50 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 50
                        denomenator = int(denomenator) / 50
                        print("numerator 50 ",numerator)
                        print("denomenator 50 ",denomenator)
                        if numerator % 50 != 0 or denomenator % 50 != 0:
                            break
                    
                if int(numerator) % 25 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 25
                        denomenator = int(denomenator) / 25
                        print("numerator 25 ",numerator)
                        print("denomenator 25 ",denomenator)
                        if numerator % 25 != 0 or denomenator % 25 != 0:
                            break
                
                if int(numerator) % 10 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 10
                        denomenator = int(denomenator) / 10
                        print("numerator 10 ",numerator)
                        print("denomenator 10 ",denomenator)
                        if numerator % 10 != 0 or denomenator % 10 != 0:
                            break
                
                if int(numerator) % 5 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 5
                        denomenator = int(denomenator) / 5
                        print("numerator 5 ",numerator)
                        print("denomenator 5 ",denomenator)
                        if numerator % 5 != 0 or denomenator % 5 != 0:
                            break
                            
                if int(numerator) % 2 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 2
                        denomenator = int(denomenator) / 2
                        print("numerator 2 ",numerator)
                        print("denomenator 2 ",denomenator)
                        if numerator % 2 != 0 or denomenator % 2 != 0:
                            break
                        
                if int(numerator) == 0:
                    numerator = ""
                    denomenator = ""
                    
                self.ids.list_of_steps.add_widget(Label(text= str(entry) + " to Fraction = ", font_size = '20sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0",""), font_size = '20sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(whole).replace(".0","") + " " + "---" * len(str(denomenator)) + "  " * len(whole), font_size = '20sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = '20sp', size_hint_y= None, height=100))
                self.layouts.append(layout) 
            else:
                self.ids.list_of_steps.add_widget(Label(text="Enter a decimal number", font_size = '20sp', size_hint_y= None, height=100))
                self.layouts.append(layout) 
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def convert_dec_to_perc(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            if entry.count(".") == 1:
                period = entry.find(".")
                first_half = entry[:period].replace("-","")
                print("first_half",first_half)
                if len(first_half) == 0:
                    first_half = "0"
                    print("first_half",first_half)
                whole = int(first_half) * 100
                print("whole",whole)
                
                second_half = entry[period+1:]
                print("second_half",second_half)
                if len(second_half) == 1:
                    second_half = second_half + "0"
                    print("second_half",second_half)
                two_digits = second_half[:2]
                print("two_digits",two_digits)
                
                other_half = second_half[2:]
                print("other_half",other_half)
                if other_half == "":
                    other_half = "0"
                    print("other_half",other_half)
                
                whole = int(whole) + int(two_digits)
                print("whole",whole)
                
                percent = str(whole) + "." + other_half + "%"
                
                if entry[0] == "-":
                    percent = "-" + percent
                    percent = percent.replace("--","-")
                    print("percent",percent)
                    
                
                self.ids.list_of_steps.add_widget(Label(text=percent, font_size = '20sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
            else:
                self.ids.list_of_steps.add_widget(Label(text="Enter a decimal number", font_size = '20sp', size_hint_y= None, height=100))
                self.layouts.append(layout) 
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)      
            
class Fractions_converter(Screen):
    def __init__(self, **kwargs):
        super(Fractions_converter, self).__init__(**kwargs)
        
    layouts = []
    def convert_frac_to_perc(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            left_par_index = entry.find("(") 
            whole = entry[:left_par_index] 
            print("whole",whole)
            frac_sign = entry.find("/")
            numerator = entry[left_par_index+1:frac_sign]
            print("numerator",numerator)
            right_par_index = entry.find(")")
            denomenator = entry[frac_sign+1:right_par_index]
            print("denomenator",denomenator)
            if numerator[0] != "-" and denomenator[0] != "-":
                if numerator == "" and denomenator == "":
                    numerator = 1
                    denomenator = 1
                if int(numerator) < int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0","") , font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(whole).replace(".0","") + " " + "---" * len(denomenator) + "  " * len(str(whole)), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= " to Percentage = ", font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    last_digits = str(int(numerator) / int(denomenator))
                    print("last_digits",last_digits)
                    if str(whole) != "":
                        if str(whole)[0] != "-":
                            percentage = str((float(whole) + float(last_digits)) * 100) + "%"
                            print("percentage",percentage)
                            self.ids.list_of_steps.add_widget(Label(text= percentage, font_size = '20sp', size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        else:
                            percentage = str((float(whole) - float(last_digits)) * 100) + "%"
                            print("percentage",percentage)
                            self.ids.list_of_steps.add_widget(Label(text= percentage, font_size = '20sp', size_hint_y= None, height=100))
                            self.layouts.append(layout)
                    else:
                        percentage = str((float(last_digits)) * 100) + "%"
                        print("percentage",percentage)
                        self.ids.list_of_steps.add_widget(Label(text= percentage, font_size = '20sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                elif int(numerator) == int(denomenator) or str(numerator) == str(denomenator):
                    whole = str(int(whole) * 100) + "%"
                    print("whole",whole)
                    self.ids.list_of_steps.add_widget(Label(text= whole, font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                    self.ids.list_of_steps.add_widget(Label(text="Numerator exceeds Denomenator", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
            else:
                self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def convert_frac_to_dec(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            left_par_index = entry.find("(") 
            whole = entry[:left_par_index] 
            print("whole",whole)
            frac_sign = entry.find("/")
            numerator = entry[left_par_index+1:frac_sign]
            print("numerator",numerator)
            right_par_index = entry.find(")")
            denomenator = entry[frac_sign+1:right_par_index]
            print("denomenator",denomenator)
            
            if numerator[0] != "-" and denomenator[0] != "-":
                if int(numerator) < int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= str(numerator), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(whole)+ " " + "---" * len(numerator) + "  " * len(str(whole)), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= " to Decimal = ", font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    last_digits = str(int(numerator) / int(denomenator))
                    print("last_digits",last_digits)
                    period = last_digits.find(".")
                    dec = last_digits[period+1:]
                    
                    decimal = str(whole) + "." + str(dec)
                    print("decimal",decimal)
                    if decimal.count(".") > 1:
                        index = decimal.find(".")
                        decimal = decimal[:index] + decimal[index+1:]
                    self.ids.list_of_steps.add_widget(Label(text= decimal, font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                  self.ids.list_of_steps.add_widget(Label(text="Numerator exceeds Denomenator", font_size = '20sp', size_hint_y= None, height=100))
                  self.layouts.append(layout)      
            else:
                  self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))
                  self.layouts.append(layout)  
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
            
class Percentages_converter(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Percentages_converter, self).__init__(**kwargs)
    
    layouts = []
    def convert_perc_to_frac(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            # 2, 4, 5, 10, 25, '15sp'
            if len(entry) > 2:
                numerator = entry[-2:]
                whole = entry[:-2]
                print("whole",whole)
                print("numerator",numerator)
                denomenator = 100
                if int(numerator) % 50 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 50
                        denomenator = int(denomenator) / 50
                        print("numerator 50",numerator)
                        print("denomenator 50 ",denomenator)
                        if numerator % 50 != 0 or denomenator % 50 != 0:
                            break
                
                if int(numerator) % 25 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 25
                        denomenator = int(denomenator) / 25
                        print("numerator 25 ",numerator)
                        print("denomenator 25 ",denomenator)
                        if numerator % 25 != 0 or denomenator % 25 != 0:
                            break

                if int(numerator) % 10 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 10
                        denomenator = int(denomenator) / 10
                        print("numerator 10 ",numerator)
                        print("denomenator 10 ",denomenator)
                        if numerator % 10 != 0 or denomenator % 10 != 0:
                            break
                
                if int(numerator) % 5 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 5
                        denomenator = int(denomenator) / 5
                        print("numerator 5 ",numerator)
                        print("denomenator 5 ",denomenator)
                        if numerator % 5 != 0 or denomenator % 5 != 0:
                            break
                
                if int(numerator) % 2 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 2
                        denomenator = int(denomenator) / 2
                        print("numerator 2 ",numerator)
                        print("denomenator 2 ",denomenator)
                        if numerator % 2 != 0 or denomenator % 2 != 0:
                            break
                        
                if str(numerator) == "00":
                    numerator = "1" + str(numerator)
                    
                if str(numerator)[0] == "0":
                    numerator = str(numerator)[1]    
                    
                if int(numerator) != int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= str(entry) + "% to Fraction = ", font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0",""), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(whole).replace(".0","") + " " + "---" * len(str(denomenator)) + "  ", font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)     
                
                if int(numerator) == int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= entry + "% to Fraction = ", font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(entry).replace(".0","") , font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "-----", font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)   
                
            if len(entry) <= 2:
                numerator = entry
                print("numerator",numerator)
                denomenator = 100
                if int(numerator) % 50 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / '15sp'
                        denomenator = int(denomenator) / '15sp'
                        print("numerator 50",numerator)
                        print("denomenator 50 ",denomenator)
                        if numerator % '15sp' != 0 or denomenator % '15sp' != 0:
                            break
                    
                if int(numerator) % 25 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 25
                        denomenator = int(denomenator) / 25
                        print("numerator 25 ",numerator)
                        print("denomenator 25 ",denomenator)
                        if numerator % 25 != 0 or denomenator % 25 != 0:
                            break
                
                if int(numerator) % 10 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 10
                        denomenator = int(denomenator) / 10
                        print("numerator 10 ",numerator)
                        print("denomenator 10 ",denomenator)
                        if numerator % 10 != 0 or denomenator % 10 != 0:
                            break
                
                if int(numerator) % 5 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 5
                        denomenator = int(denomenator) / 5
                        print("numerator 5 ",numerator)
                        print("denomenator 5 ",denomenator)
                        if numerator % 5 != 0 or denomenator % 5 != 0:
                            break
                            
                if int(numerator) % 2 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 2
                        denomenator = int(denomenator) / 2
                        print("numerator 2 ",numerator)
                        print("denomenator 2 ",denomenator)
                        if numerator % 2 != 0 or denomenator % 2 != 0:
                            break
                        
                if str(numerator)[0] == "0":
                    numerator = str(numerator)[1]
                    
                if int(numerator) != int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= str(entry) + "% to Fraction = ", font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0",""), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "----", font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)     
                    
                if int(numerator) == int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= entry + "% to Fraction = ", font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(entry).replace(".0","") , font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "-----", font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)  
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def convert_perc_to_dec(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            dec = entry + "/100"
            evaled = str(eval(dec))
            print("evaled",evaled)
            self.ids.list_of_steps.add_widget(Label(text= entry + "% to Decimal = ", font_size = '20sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= evaled, font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))   
            self.layouts.append(layout)


#Percentage_Calculator
Builder.load_string("""
<Statistical_Calculator>
    id:Statistical_Calculator
    name:"Statistical_Calculator"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Statistical Calculator"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        perc.text = ""
                        dev.text = ""
                        list_of_steps.clear_widgets()       
        
            TextInput:
                id: entry
                text: entry.text
                hint_text: "Numbers seperated by a comma"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10
            
                    
            Button:
                id: mmm
                text: "Mean, Median & Mode"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Statistical_Calculator.mmm(entry.text)    
                
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                    
                TextInput:
                    id: dev
                    text: dev.text
                    hint_text: "1,2 or 3 Deviations"
                    multiline: False
                    font_size: '15sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:1 - len(dev.text)] 
                    
                Button:
                    id: sd
                    text: "Standard Deviation"   
                    font_size: '15sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Statistical_Calculator.sd(entry.text + "&" + dev.text)  
                    
            Button:
                id: var
                text: "Variance"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Statistical_Calculator.var(entry.text)  
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                    
                TextInput:
                    id: perc
                    text: perc.text
                    hint_text: "nth Percentile"
                    multiline: False
                    font_size: '15sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:3 - len(perc.text)] 
                    
                Button:
                    id: percentile
                    text: "Percentile"   
                    font_size: '15sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Statistical_Calculator.perc(entry.text + "%" + perc.text)  
                          
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Statistical_Calculator(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Statistical_Calculator, self).__init__(**kwargs)
            
    layouts = []
    def mmm(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
            self.ids.list_of_steps.add_widget(Label(text= "Entry = " + entry.replace(" ","").replace(",",", ") ,font_size = '15sp', size_hint_y= None, height=100))

            entry_list = entry.split(",")
            print("entry_list",entry_list)
            
            i=0
            while i < len(entry_list):
                entry_list[i] = float(entry_list[i])
                i = i + 1
            
            mean_output = str(np.mean(entry_list))
            print("Mean: ",mean_output)
            
            median_output = str(np.median(entry_list))
            print("Median: ",median_output)
            
            #Mean
            entry_list_count = []
            i = 0
            while i < len(entry_list):
                print("loop started")
                print("entry_list",entry_list[i])
                entry_list_count.append(entry_list.count(entry_list[i]))
                print("entry_list_count",entry_list_count)
                i = i + 1
                
            print()
            maximum_count = max(entry_list_count)
            print("maximum_count",maximum_count)
            maximum_count_index = entry_list_count.index(maximum_count)
            print("maximum_count_index",maximum_count_index)
            mode_output = entry_list[maximum_count_index]
            print("mode_output",mode_output)
                
                
            self.ids.list_of_steps.add_widget(Label(text= "Mean = " + mean_output ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "Median = " + median_output ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "Mode = " + str(mode_output) + " counted " + str(maximum_count) + " time(s) ",font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
            
    def sd(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
            amp = entry.find("&")
            print("amp:",amp)
            
            self.ids.list_of_steps.add_widget(Label(text= "Entry = " + entry[:amp].replace(" ","").replace(",",", ") ,font_size = '15sp', size_hint_y= None, height=100))
            
            dev = entry[amp+1:]
            print("dev:",dev)
            
            if dev == "":
                dev = 1
            
            entry_list = entry[:amp].split(",")
            print("entry_list",entry_list)
            
            i=0
            while i < len(entry_list):
                entry_list[i] = float(entry_list[i])
                i = i + 1
            
            if int(dev) == 1:
                SD = entry_list
                SD = str(np.std(SD))
                print("SD",SD)
                self.ids.list_of_steps.add_widget(Label(text= "Standard Deviation = " ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= SD ,font_size = '15sp', size_hint_y= None, height=100))

            elif int(dev) == 2:
                SD = entry_list
                SD = str(float(np.mean(entry_list)) + 2 * float(np.std(SD)))
                print("SD",SD)
                self.ids.list_of_steps.add_widget(Label(text= "Second Standard Deviation = ",font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= SD ,font_size = '15sp', size_hint_y= None, height=100))
            
            elif int(dev) == 3:
                SD = entry_list
                SD = str(float(np.mean(entry_list)) + 3 * float(np.std(SD)))
                print("SD",SD)
                self.ids.list_of_steps.add_widget(Label(text= "Third Standard Deviation = " ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= SD ,font_size = '15sp', size_hint_y= None, height=100))
                
            elif int(dev) > 3:
                self.ids.list_of_steps.add_widget(Label(text= "Standard Deviation must be between :" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "1, 2 or 3" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def var(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:

            self.ids.list_of_steps.add_widget(Label(text= "Entry = " + entry.replace(" ","").replace(",",", ") ,font_size = '15sp', size_hint_y= None, height=100))

            entry_list = entry.split(",")
            print("entry_list",entry_list)
            
            i=0
            while i < len(entry_list):
                entry_list[i] = float(entry_list[i])
                i = i + 1
            
            var = str(np.var(entry_list))
            print("Var",var)
            
            self.ids.list_of_steps.add_widget(Label(text= "Variance = " + var ,font_size = '15sp', size_hint_y= None, height=100))
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def perc(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:

            print("entry",entry)
            percent = entry.find("%")
            print("percent",percent)
            
            self.ids.list_of_steps.add_widget(Label(text= "Entry = " + entry[:percent].replace(" ","").replace(",",", ") ,font_size = '15sp', size_hint_y= None, height=100))
            
            nth = int(entry[percent+1:])
            print("nth",nth)
            
            entry = entry[:percent]
            print("entry",entry)
            
            entry_list = entry.split(",")
            print("entry_list",entry_list)
            
            i=0
            while i < len(entry_list):
                entry_list[i] = float(entry_list[i])
                i = i + 1
            
            perc = str(np.percentile(entry_list,nth))
            print("perc",perc)
            
            if str(nth)[-1] == "1":
                nth = str(nth) + "st"
            elif str(nth)[-1] == "2":
                nth = str(nth) + "nd"
            elif str(nth)[-1] == "3":
                nth = str(nth) + "rd"
            else:
                nth = str(nth) + "th"
            print("nth",nth)
            
            self.ids.list_of_steps.add_widget(Label(text= perc + " is in the " + str(nth) + " Percentile"  ,font_size = '15sp', size_hint_y= None, height=100))
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
                

#FOIL
Builder.load_string("""
<FOIL>
    id:FOIL
    name:"FOIL"
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "FOIL Method"
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        list_of_steps.clear_widgets()            
                    
            TextInput:
                id: entry
                text: entry.text
                multiline: False
                hint_text: "(ax + b)(cx + d)"
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10
                
            Button:
                markup: True
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    FOIL.steps(entry.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

class FOIL(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(FOIL, self).__init__(**kwargs)
            
    layouts = []
    def steps(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            a = entry.lower()
            a = a.replace(" ","")
            a = a.replace("+-","-")
            a = a.replace(")*(",")(")
            a = a.replace("+"," + ")
            a = a.replace("-"," - ")
            a = a.replace("**","^")
            a = a.replace("( - ","(-")
            a = a.replace("*"," * ")
            
            # Split string method to Highlight each step in green before evaluation
            a_list = a.replace(")("," ").replace("(","").replace(")","")
            a_list = a_list.split(" ")
            print(a_list)
            
            print()
            print("Expression entered:  ",a)
            print()
            
            self.ids.list_of_steps.add_widget(Label(text= "Expression Entered: " + a ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            x = Symbol('x')
            a = a.replace("x","*x")
            
            i = 0
            if a.count("(") == a.count(")"):
            # String Method to find FIRST
                #print("FIRST")
                while i < 1:
                    #print(a)
                    first_left_par = a.find("(")
                    first_right_par = a.find(")")
                    second_left_par = a.rfind("(")
                    second_right_par = a.rfind(")")
                    if a == " / ":
                        print("Invalid Input, no division in or outside of parentheses for Foil Methed")
                        break
                    if a == " * ":
                        print("Invalid Input, no multiplication within parentheses for Foil Method")
                        break
                    
                    right_par_left_side = a.find(")")
                    #print('right_par_left_side',right_par_left_side)
                    left_par_left_side = a[:right_par_left_side].rfind("(")
                    #print('left_par_left_side',left_par_left_side)
                    left_par_range = a[left_par_left_side:right_par_left_side+1]
                    #print('left_par_range: ',left_par_range)
                    
                    j = 0
                    while j < 1:
                        if left_par_range == " + " or "+": #  Find Add Sign
                            first_sign = left_par_range.rfind("+")
                            if first_sign == -1:
                                break
                            #sign = left_par_range.rfind("-")
                            #print("add_sign index: ",first_sign)
                            First_left = a[left_par_left_side+1:first_sign-1]
                            print("First_left",First_left)
                            if First_left == "*x":
                                First_left = "1*x"
                            next_par_range = a[right_par_left_side+1:]
                            #print('next_par_range',next_par_range)
                            left_par_right_side = next_par_range[:].find("(")
                            #print('next_par index',left_par_right_side)
                            right_par_right_side = next_par_range[:].find(")") #First Right Par
                            #print('right_par_right_side',right_par_right_side)
                            first_space_index = next_par_range[:].find(" ")
                            #print('first_space_index',first_space_index)
                            First_right = next_par_range[left_par_right_side+1:first_space_index+1]
                            print('First_right',First_right)# Use for Highlight
                            if First_right == "*x ":
                                First_right = "1*x"
                            #print()
                            #print("First Type ",type(First))
                            FIRST_DISPLAY = "FIRST: (" + '[color=33CAFF]' + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + '[color=33CAFF]' + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")"
                            self.ids.list_of_steps.add_widget(Label(text= FIRST_DISPLAY , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print('FIRST                ',"(" + Back.GREEN + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + Back.GREEN + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")")         #print("First Type ",type(First))
                            print()
                            First = First_left + " * " + First_right
                            First = First.replace("+-","-").replace("^","**")
                            #print("First Type ",type(First))
                            #First = sympify(First)
                            #print('type',type(First))
                            First = str(First).replace("^","**")
                            print("First",First)
                            First_evaled = str(eval(First))
                            First = str(First).replace("**","^").replace("*-"," * -")
                            
                            FIRST_MULTIPLY = "Multiply: " + First.replace("*x","x").replace("**","^").replace("*"," * ") + " = " + '[color=33CAFF]' + First_evaled.replace("*x","x").replace("**","^") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= FIRST_MULTIPLY , markup=True, font_size = '15sp', size_hint_y= None, height=100))

                            print("Multiply:            ", First.replace("*x","x").replace("**","^").replace("*"," * ")," = ",Back.GREEN,First_evaled,Style.RESET_ALL)   
                            print()
                            #print('                  ',First_evaled)
                            highlight_first = First_evaled.replace("**","^").replace("*","").replace("-+","-")
                            print('Expression:          ',Back.BLUE,highlight_first,Style.RESET_ALL)
                            
                            FIRST_EXPRESSION = 'Expression: ' + '[color=33CAFF]' + highlight_first + "[/color]"
                            self.ids.list_of_steps.add_widget(Label(text= FIRST_EXPRESSION , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            
                            print()
                            self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
                            print()
                            
                            break
                    if first_sign == -1: #  Find Minus Sign
                        first_sign = left_par_range.rfind("-")
                        #sign = left_par_range.find("+")
                        #print("minus_sign index: ",first_sign)
                        First_left = a[left_par_left_side+1:first_sign-1]
                        if First_left == "*x":
                            First_left = "-1*x"
                        #print('First_left',First_left) # Use for Highlight
                        next_par_range = a[right_par_left_side+1:]
                        #print('next_par_range',next_par_range)
                        left_par_right_side = next_par_range[:].find("(")
                        #print('next_par index',left_par_right_side)
                        right_par_right_side = next_par_range[:].find(")") #First Right Par
                        #print('right_par_right_side',right_par_right_side)
                        first_space_index = next_par_range[:].find(" ")
                        #print('first_space_index',first_space_index)
                        First_right = next_par_range[left_par_right_side+1:first_space_index+1]
                        if First_right == "*x":
                            First_right = "-1*x"
                        #print('First_right',First_right)# Use for Highlight
                        #print()
                        First = First_left + " * " + First_right
                        print('FIRST                ',"(" + Back.GREEN + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + Back.GREEN + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")")         #print("First Type ",type(First))
                        FIRST_DISPLAY = "FIRST: (" + '[color=33CAFF]' + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + '[color=33CAFF]' + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")"
                        self.ids.list_of_steps.add_widget(Label(text= FIRST_DISPLAY , markup=True, font_size = '15sp', size_hint_y= None, height=100))

                        #print('type',type(First))
                        First = str(First).replace(" ","").replace("+-","-").replace('--',"+").replace("-+","-").replace("^","**")
                        #x,y,z = symbols('x,y,z')
                        First_evaled = str(eval(First))
                        print()
                        First = str(First).replace("**","^").replace("*-"," * -")
                        First_evaled = First_evaled.replace("**","^")
                        
                        FIRST_MULTIPLY = "Multiply: " + First.replace("*x","x").replace("**","^").replace("*"," * ") + " = " + '[color=33CAFF]' + First_evaled.replace("*x","x").replace("**","^") + '[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= FIRST_MULTIPLY , markup=True, font_size = '15sp', size_hint_y= None, height=100))

                        print("Multiply:            ", First.replace("*x","x").replace("**","^").replace("*"," * ")," = ",Back.GREEN,First_evaled,Style.RESET_ALL)  
                        print()
                        #print('                  ',First_evaled)
                        highlight_first = First_evaled.replace("**","^").replace("*","")
                        #print()
                        print('Expression:          ',Back.BLUE,highlight_first,Style.RESET_ALL)
                        
                        FIRST_EXPRESSION = 'Expression: ' + '[color=33CAFF]' + highlight_first + "[/color]"
                        self.ids.list_of_steps.add_widget(Label(text= FIRST_EXPRESSION , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        
                        print()
                        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        print()
                            
                        break
                    i = i + 1
            # String method for OUTSIDE
                i = 0
                while i < 1:
                    if next_par_range == "+" or  "-":
                        sign_index = next_par_range.find("+")
                        if sign_index == -1:
                            sign_index = next_par_range.rfind("-")
                        #print('sign_index',sign_index)
                    Outside_right = next_par_range[sign_index:right_par_right_side]
                    Outside_right = Outside_right.replace("+","").replace(" ","").strip()
                    #print("Outside_right",Outside_right)
                    if Outside_right == "*x":
                        Outside_right = "1*x"
                    elif Outside_right == "+ *x":
                        Outside_right = "1*x"
                    elif Outside_right == "- *x":
                        Outside_right = "-1*x"
                    Outside = First_left + " * " + Outside_right
                    print('OUTSIDE              ',"(" + Back.GREEN + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")")         #print("First Type ",type(First))
                    
                    OUTSIDE_DISPLAY = "OUTSIDE: (" + '[color=33CAFF]' + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")"
                    self.ids.list_of_steps.add_widget(Label(text= OUTSIDE_DISPLAY , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    
                    evaled_Outside = str(Outside).replace("^","**")
                    evaled_Outside = eval(evaled_Outside)
                    Outside = Outside.replace("^","**")
                    evaled_Outside = str(evaled_Outside).replace("**","^")
                    print()
                    print("Multiply:            ",Outside.replace("**","^").replace("*x","x")," = ",Back.GREEN,evaled_Outside,Style.RESET_ALL)
                    
                    OUTSIDE_MULTIPLY = "Multiply: " + Outside.replace("**","^").replace("*x","x") + " = " + '[color=33CAFF]' + evaled_Outside + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= OUTSIDE_MULTIPLY , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    
                    #print()
                    #print('evaled_Outside',evaled_Outside)
                    #print()
                    highlight_Outside = str(evaled_Outside).replace(" ","").replace("**","^").replace("*","").replace("-"," - ").strip()
                    
                    if highlight_Outside[0] != "-":
                        highlight_Outside = " + " + highlight_Outside
                    print()
                    print("Expression:          ",Back.BLUE,highlight_first,Style.RESET_ALL,Back.GREEN,highlight_Outside,Style.RESET_ALL)
                    
                    OUTSIDE_HIGHLIGHT = "Expression: " + '[color=33CAFF]'  + highlight_first + highlight_Outside + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= OUTSIDE_HIGHLIGHT , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    
                    print()
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print()
                    
                    break
            
            # String Method for INSIDE
                i = 0
                while i < 1:        
                    INSIDE_left = left_par_range[first_sign:right_par_left_side]
                    INSIDE_left = INSIDE_left.replace("^","**")
                    print(INSIDE_left)
                    if INSIDE_left == "+ *x":
                        INSIDE_left = "1*x"
                    elif INSIDE_left == "- *x":
                        INSIDE_left = "-1*x"
                    Inside_sign = left_par_range.find("+")
                    if Inside_sign == -1:
                        Inside_sign = left_par_range.rfind("-")
                        
                    #print("INSIDE_left",INSIDE_left) 
                    #print("Inside_sign index",Inside_sign)
                    Inside_sign_right_side = next_par_range.find("+")
                    if Inside_sign_right_side == -1:
                        Inside_sign_right_side = next_par_range.rfind("-")
                    print('INSIDE               ',"(" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")(" + Back.GREEN + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")")         #print("First Type ",type(First))
                    
                    INSIDE_DISPLAY = "INSIDE (" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")(" + '[color=33CAFF]' + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")"
                    self.ids.list_of_steps.add_widget(Label(text= INSIDE_DISPLAY , markup=True, font_size = '15sp', size_hint_y= None, height=100))

                    Inside =  INSIDE_left + " * " + First_right
                    Inside = Inside.replace("^","**")
                    if Inside == "*x":
                        Inside = "1*x"
                    print()
                    Inside_evaled = str(eval(Inside)).replace(" ","").replace("**","^").replace("+"," +").strip()
                    Inside = Inside.replace("**","^")
                    Inside_evaled = str(Inside_evaled).replace("**","^")
                    Inside_evaled = Inside_evaled.replace("+-","-")
                    print("Multiply:            ",Inside.replace("*x","x").replace("**","^")," = ",Back.GREEN,Inside_evaled,Style.RESET_ALL)
                    print()
                    
                    INSIDE_MULTIPLY = "Multiply: " + Inside.replace("*x","x").replace("**","^") + " = " + '[color=33CAFF]' + Inside_evaled + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= INSIDE_MULTIPLY , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    
                    #print("Inside_evaled",Inside_evaled)
                    highlight_Inside = Inside_evaled.replace("*","").replace(" ","")

                    if highlight_Inside[0] != "-":
                        highlight_Inside = " + " + highlight_Inside
                    print("Expression:         ",Back.BLUE,highlight_first,highlight_Outside,Style.RESET_ALL,Back.GREEN,highlight_Inside,Style.RESET_ALL)
                    
                    INSIDE_HIGHLIGHT = "Expression: " + '[color=33CAFF]' + highlight_first + highlight_Outside + highlight_Inside + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= INSIDE_HIGHLIGHT , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    print()
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print()
                    break
                
            # String Method for LAST
                i = 0 
                while i < 1:
                    print('LAST                 ',"(" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")")         #print("First Type ",type(First))
                    print()
                    
                    LAST_DISPLAY = "LAST: (" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")"
                    self.ids.list_of_steps.add_widget(Label(text= LAST_DISPLAY , markup=True, font_size = '15sp', size_hint_y= None, height=100))

                    Last = INSIDE_left + " * " + Outside_right 
                    Last = Last.replace("^","**")
                    if Last == "*x":
                        Last = "1*x"
                    Last_evaled = str(eval(Last)).replace(" ","").replace("**","^").replace("-","- ").strip()
                    Last = Last.replace("^","**")
                    Last_evaled = str(Last_evaled).replace("**","^")
                    print("Multiply:            ",Last.replace("*x","x").replace("**","^")," = ",Back.GREEN,Last_evaled,Style.RESET_ALL)
                    print()
                    #print('Last_evaled',Last_evaled)
                    
                    LAST_MULTIPLY = "Multiply: " + Last.replace("*x","x").replace("**","^") + " = " + '[color=33CAFF]' + Last_evaled + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= LAST_MULTIPLY , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    
                    highlight_Last = Last_evaled.replace("*","")#.replace("-","- ")
            
                    if highlight_Last[0] != "-":
                        highlight_Last = " + " + highlight_Last
            
                    print("Expression:         ",Back.BLUE,highlight_first,highlight_Outside,highlight_Inside,Style.RESET_ALL,Back.GREEN,highlight_Last,Style.RESET_ALL)
                    LAST_EXPRESSION = "Expression: " + '[color=33CAFF]' + highlight_first + highlight_Outside + highlight_Inside + highlight_Last + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= LAST_EXPRESSION , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    print()
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print()        
                    break
                
                FOIL = str(First_evaled) + "+" + str(evaled_Outside) + "+" + str(Inside_evaled) + "+" + str(Last_evaled)
                FOIL = FOIL.strip().replace("**","^").replace(" ","").replace("+-","-").replace("+"," + ").replace("-"," - ").replace("*","")
                print("Expression FOILed:  ",Back.BLUE,FOIL,Style.RESET_ALL)
                EXPRESSION_FOLIED = '[color=33CAFF]' + FOIL + '[/color]'
                self.ids.list_of_steps.add_widget(Label(text= "Expression FOILed:  ", markup=True, font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= EXPRESSION_FOLIED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                print()
                self.ids.list_of_steps.add_widget(Label(text= "Next, combine like terms" , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                print("Next, combine like terms")
                print()
                self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()  
                
                First_evaled = str(First_evaled).replace("^","**")
                evaled_Outside = "+" + str(evaled_Outside).replace("^","**")
                Inside_evaled =  "+" + str(Inside_evaled).replace("^","**")
                Last_evaled =  "+" + str(Last_evaled).replace("^","**")
                First_evaled =  str(First_evaled).replace("+-","-")
                evaled_Outside = str(evaled_Outside).replace("+-","-")
                Inside_evaled =   str(Inside_evaled).replace("+-","-")
                Last_evaled =  str(Last_evaled).replace("+-","-")
                
                #print("aLL CURRENTLY    ",First_evaled," ",evaled_Outside," ",Inside_evaled," ",Last_evaled)
                answer = ""
                combine_evaled_FOIL = ""
                combine_evaled_FO = ""
                combine_evaled_IL = ""
                combine_evaled_FI = ""
                combine_evaled_OL = ""
                combine_evaled_FL = ""
                combine_evaled_OI = ""
            # Combine Like Terms if all can combine
            
                
            #Combine like Terms
            #First evaled, check for if Exponent, Variable, Integer
                First_evaled = First_evaled.replace("**","^")
                evaled_Outside = evaled_Outside.replace("**","^")
                Inside_evaled = Inside_evaled.replace("**","^")
                Last_evaled = Last_evaled.replace("**","^")
                
                exponent_First_evaled = " "
                variable_First_evaled = " "
                integer_First_evaled = " "
                
                exponent_evaled_Outside = " "
                variable_Outside_evaled = " "
                integer_evaled_Outside = " "
                
                exponent_Inside_evaled = " "
                variable_Inside_evaled = " "
                integer_Inside_evaled = " "
                
                exponent_Last_evaled = " "
                variable_Last_evaled = " "
                integer_Last_evaled = " "
                
                non_combine = 0
                
                i = 0
                while i < 1: #Highlight each possible combo
                    if First_evaled.count("^") == 1:
                        exponent_First_evaled = First_evaled.replace("^","**")
                        print(First_evaled.replace("*",""),"is an exponent")
                        carrot = First_evaled.find("^")
                        exponent_First = First_evaled[carrot+1:]
                        print("exponent_First",exponent_First)
                        
                    if evaled_Outside.count("^") == 1:
                        exponent_evaled_Outside = evaled_Outside.replace("^","**")
                        print(evaled_Outside, "Its an exponent")
                        carrot = evaled_Outside.find("^")
                        exponent_Outside = evaled_Outside[carrot+1:]
                        print("exponent_First",exponent_Outside)
                        
                    if Inside_evaled.count("^") == 1:
                        exponent_Inside_evaled = Inside_evaled.replace("^","**")
                        print(Inside_evaled,"Its an exponent")
                        carrot = Inside_evaled.find("^")
                        exponent_Inside = Inside_evaled[carrot+1:]
                        print("exponent_First",exponent_Inside)
                        
                    if Last_evaled.count("^") == 1:
                        exponent_Last_evaled = Last_evaled.replace("^","**")
                        print(Last_evaled,"Its an exponent")
                        carrot = Last_evaled.find("^")
                        exponent_Last = Last_evaled[carrot+1:]
                        print("exponent_First",exponent_Last)
                    
                    if exponent_First_evaled != " " and exponent_evaled_Outside  != " " and exponent_Inside_evaled != " " and exponent_Last_evaled != " ":
                        print("1Combine terms:      ",Back.BLUE,First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + "),evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: " + '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ") + evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' 
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     ",Back.BLUE,str(eval(exponent_First_evaled + exponent_evaled_Outside + exponent_Inside_evaled + exponent_Last_evaled)).replace("*","").replace("**","^"),Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled + exponent_evaled_Outside + exponent_Inside_evaled + exponent_Last_evaled)).replace("**","^").replace("**","^") + '[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    if exponent_First_evaled != " " and exponent_evaled_Outside  != " ":
                        print()
                        print("exponent_First_evaled",exponent_First_evaled)
                        print("exponent_evaled_Outside",exponent_evaled_Outside)
                        print()
                        if exponent_First_evaled[-1] == exponent_evaled_Outside[-1]:
                            print("2Combine terms:      ",Back.BLUE,First_evaled.replace(" ","").replace("**","^").replace("*",""),evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Style.RESET_ALL,Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                            COMBINE_TERMS = "Combine terms: " + '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*",""),evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' + Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     ",Back.BLUE,str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," "),Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_First_evaled != " " and exponent_Inside_evaled  != " ":
                        print()
                        print("exponent_First_evaled",exponent_First_evaled)
                        print("exponent_Inside_evaled",exponent_Inside_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Inside_evaled[-1]:
                            print("3Combine terms: "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                            COMBINE_TERMS = "Combine terms: "+ '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ") + '[/color]' + evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[color=33CAFF]' + Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_First_evaled +" + "+ exponent_Inside_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_First_evaled != " " and exponent_Last_evaled  != " ":
                        print()
                        print("exponent_First_evaled",exponent_First_evaled)
                        print("exponent_Last_evaled",exponent_Last_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("4Combine terms: "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                            COMBINE_TERMS = "Combine terms: " + '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ") + '[/color]' + evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_First_evaled +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_evaled_Outside != " " and exponent_Inside_evaled  != " ":
                        print()
                        print("exponent_evaled_Outside",exponent_evaled_Outside)
                        print("exponent_Inside_evaled",exponent_Inside_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("5Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                            COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+ '[color=33CAFF]' +evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+ '[/color]' +Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_evaled_Outside +" + "+ exponent_Inside_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: "+ '[color=33CAFF]' +str(eval(exponent_evaled_Outside +" + "+ exponent_Inside_evaled)).replace("*","").replace("**","^")+'[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_evaled_Outside != " " and exponent_Last_evaled != " ":
                        print()
                        print("exponent_evaled_Outside",exponent_evaled_Outside)
                        print("exponent_Last_evaled",exponent_Last_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("6Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                            COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+ '[color=33CAFF]' +evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+ '[/color]' +Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[color=33CAFF]' + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_evaled_Outside +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: "+ '[color=33CAFF]' +str(eval(exponent_evaled_Outside +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+ '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_Inside_evaled != " " and exponent_Last_evaled != " ":
                        print()
                        print("exponent_Inside_evaled",exponent_Inside_evaled)
                        print("exponent_Last_evaled",exponent_Last_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("7Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)        
                            COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_Inside_evaled +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]' + str(eval(exponent_Inside_evaled +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+ '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    non_combine = non_combine + 1
                    break
                i = 0
                while i < 1:
                    if First_evaled.count("x") == 1 and First_evaled.count("^") == 0:
                        variable_First_evaled = First_evaled
                        print("Its a variable F"+variable_First_evaled)
                    if evaled_Outside.count("x") == 1 and evaled_Outside.count("^") == 0:
                        variable_Outside_evaled = evaled_Outside
                        print("Its a variable O"+variable_Outside_evaled)
                    if Inside_evaled.count("x") == 1 and Inside_evaled.count("^") == 0:
                        variable_Inside_evaled = Inside_evaled
                        print("Its a variable I"+variable_Inside_evaled)
                    if Last_evaled.count("x") == 1 and Last_evaled.count("^") == 0:
                        variable_Last_evaled = Last_evaled
                        print("Its a variable L"+variable_Last_evaled)
            
                    if variable_First_evaled != " " and variable_Outside_evaled  != " " and variable_Inside_evaled != " " and variable_Last_evaled != " ":
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+ '[/color]' 
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled +" + "+ variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled +" + "+ variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","").replace("**","^")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    if variable_First_evaled != " " and variable_Outside_evaled != " " :
                        print()
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_First_evaled != " " and variable_Inside_evaled != " " :
                        print()
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_First_evaled != " " and variable_Last_evaled != " " :
                        print()
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_Outside_evaled != " " and variable_Inside_evaled != " " :
                        print()
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_Outside_evaled +" + "+ variable_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_Outside_evaled +" + "+ variable_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_Outside_evaled != " " and variable_Last_evaled != " " :
                        print()
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_Outside_evaled +" + "+ variable_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_Outside_evaled +" + "+ variable_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_Inside_evaled != " " and variable_Last_evaled != " " :
                        print()
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    non_combine = non_combine + 1
                    break
            
                i = 0
                while i < 1:
                    if First_evaled.count("x") == 0 and First_evaled.count("^") == 0:
                        integer_First_evaled =  First_evaled
                        print("Its an integer F")
                    if evaled_Outside.count("x") == 0 and evaled_Outside.count("^") == 0:
                        integer_evaled_Outside =  evaled_Outside
                        print("Its an integer O")
                    if Inside_evaled.count("x") == 0 and Inside_evaled.count("^") == 0:
                        integer_Inside_evaled =  Inside_evaled
                        print("Its an integer I")
                    if Last_evaled.count("x") == 0 and Last_evaled.count("^") == 0:
                        integer_Last_evaled =  Last_evaled
                        print("Its an integer L")
                      
                    if integer_First_evaled != " " and integer_evaled_Outside  != " " and integer_Inside_evaled != " " and integer_Last_evaled != " ":
                        print("FOIL")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside +" + "+ integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside +" + "+ integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*","").replace("**","^")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    if integer_First_evaled != " " and integer_evaled_Outside != " " :
                        print()
                        print("FO")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_First_evaled != " " and integer_Inside_evaled != " " :
                        print()
                        print("FI")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_First_evaled != " " and integer_Last_evaled != " " :
                        print()
                        print("FL")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_evaled_Outside != " " and integer_Inside_evaled != " " :
                        print()
                        print("OI")
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_evaled_Outside +" + "+ integer_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_evaled_Outside +" + "+ integer_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_evaled_Outside != " " and integer_Last_evaled != " " :
                        print()
                        print("OL")
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_evaled_Outside +" + "+ integer_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_evaled_Outside +" + "+ integer_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_Inside_evaled != " " and integer_Last_evaled != " " :
                        print()
                        print("IL")
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)        
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'  
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*"+"")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    non_combine = non_combine + 1
                    break
                
                if non_combine == 3:
                    print("No terms to combine")
                    self.ids.list_of_steps.add_widget(Label(text= "No terms to combine" , markup=True, font_size = '15sp', size_hint_y= None, height=100))
                    
                exponents_evaled_list = [exponent_First_evaled,exponent_evaled_Outside,exponent_Inside_evaled,exponent_Last_evaled]
                #print("exponents_evaled_list",exponents_evaled_list)
                #print()
                add_up_exponents = exponent_First_evaled + exponent_evaled_Outside + exponent_Inside_evaled + exponent_Last_evaled
                add_up_exponents = add_up_exponents.replace(" ","").replace("**","^")
                combined_exponents = ""
                if add_up_exponents.count("^") > 0:
                    add_up_exponents = add_up_exponents.replace("^","**").replace(" ","")
                    combined_exponents = str(eval(add_up_exponents)).replace("**","^")
                #print(combined_exponents.replace("**","^").replace("*",""))
                
                First_evaled_exp_index = exponent_First_evaled.find("^")
                #print("First_evaled_exp_index",First_evaled_exp_index)
                
                #print()
                variables_evaled_list = [variable_First_evaled,variable_Outside_evaled,variable_Inside_evaled,variable_Last_evaled]
                #print("variables_evaled_list",variables_evaled_list)
                #print()
                add_up_variables = variable_First_evaled + variable_Outside_evaled + variable_Inside_evaled + variable_Last_evaled
                add_up_variables = add_up_variables.strip().replace(" ","")
                combined_variables = ""
                if add_up_variables.count("x") > 0:
                    combined_variables = str(eval(add_up_variables))
                #print("combined_variables",combined_variables)
                #print()
                
                #integers_evaled_list = [integer_First_evaled,integer_evaled_Outside,integer_Inside_evaled,integer_Last_evaled]
                #print("integers_evaled_list",integers_evaled_list)
                #print()
                add_up_integers = integer_First_evaled + integer_evaled_Outside + integer_Inside_evaled + integer_Last_evaled
                #print("add_up_integers length",len(add_up_integers.replace(" ","")))
                combined_integers = ""
                add_up_integers = add_up_integers.strip().replace(" ","")
                if len(add_up_integers.replace(" ","")) != 0:
                   combined_integers = str(eval(add_up_integers))
                #print("combined_variables",combined_integers)
                
                FINAL_ANSWER = (str(combined_exponents) + "+" + str(combined_variables) + "+" + str(combined_integers)).replace("*","").replace("++","")
                print("FINAL_ANSWER: ",FINAL_ANSWER)
                if FINAL_ANSWER[-1] == "+" or FINAL_ANSWER[-1] == "-":
                    FINAL_ANSWER = FINAL_ANSWER[:-1]
                FINAL_ANSWER = FINAL_ANSWER.replace("+-","-").replace("-"," - ").replace("+"," + ").replace("*","")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()
                print("Answer in order:    ",FINAL_ANSWER)
                self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Final Answer: " + FINAL_ANSWER.replace("*","") ,font_size = '15sp', size_hint_y= None, height=100))
                
            else:
                print("Parentheses Unbalanced")
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
#Tip calc
Builder.load_string("""
<Tip_Calculator>
    id:Tip_Calculator
    name:"Tip_Calculator"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Tip Calculator"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        Bill.text = ""
                        Percent.text = ""
                        Split.text = ""
                        list_of_steps.clear_widgets()       
                                   
            TextInput:
                id: Bill
                text: Bill.text
                hint_text: "Bill: $"
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10
                input_filter: lambda text, from_undo: text[:6 - len(Bill.text)]           
        
            TextInput:
                id: Percent
                text: Percent.text
                hint_text: "Percent: %"
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10              
                input_filter: lambda text, from_undo: text[:2 - len(Percent.text)]         
                
            TextInput:
                id: Split
                text: Split.text
                hint_text: "Split:"
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 200
                padding: 10              
                input_filter: lambda text, from_undo: text[:3 - len(Split.text)] 
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Tip_Calculator.steps(Bill.text + "$" + Percent.text + "&" + Split.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Tip_Calculator(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Tip_Calculator, self).__init__(**kwargs)
            
    layouts = []
    def steps(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            # Tip Calculator
            print("~~~~~~~~~~~~~~~~")
            print(entry)
            bill = entry[:entry.find("$")]
            print()
            print("Bill",bill)
            perc = entry[entry.find("$")+1:entry.find("&")]
            
            if perc == "":
                perc = 0
                print("perc",perc)
            
            tip = str(float(bill) * float(perc) / 100)
            print()
            print("Tip: $",tip)
            
            total = str(float(bill) + (float(bill) * float(perc) / 100))
            print()
            print("Total Bill: $", total)
            
            split = entry[entry.find("&")+1:]
            print()
            print("split",split)
            
            if split == "":
                split = 0
                print()
                print("Split:",split)
            
            if int(split) > 1:
                bill_split = str(float(bill) / float(split))
                print("Bill split", bill_split)
                
                tip_split = str(float(tip) / float(split))
                print("tip_split",tip_split)
                
                total_split = str(float(total) / float(split))
                print("total_split",total_split)
                
                self.ids.list_of_steps.add_widget(Label(text= "Bill = $" + "{:,.2f}".format(float(bill)) ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                 
                self.ids.list_of_steps.add_widget(Label(text= "Percent for Tip = " + str(perc) + "%" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                 
                self.ids.list_of_steps.add_widget(Label(text= "Tip = $" + "{:,.2f}".format(float(tip)),font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                self.ids.list_of_steps.add_widget(Label(text= "Total Bill = $" + "{:,.2f}".format(float(total)),font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout) 

            
            if float(split) == 1 or float(split) == 0: 
                self.ids.list_of_steps.add_widget(Label(text= "Bill = $" + "{:,.2f}".format(float(bill)) ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                 
                self.ids.list_of_steps.add_widget(Label(text= "Percent for Tip = " + str(perc) + "%" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                self.ids.list_of_steps.add_widget(Label(text= "Tip = $" + "{:,.2f}".format(float(tip)),font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                self.ids.list_of_steps.add_widget(Label(text= "Total Bill = ${:,.2f}".format(float(total)) ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            elif float(split) > 1:
                self.ids.list_of_steps.add_widget(Label(text= "${:,.2f}".format(float(bill)) + " bill split " + str(split) + " ways = ${:,.2f}".format(float(bill_split)) ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                self.ids.list_of_steps.add_widget(Label(text= "${:,.2f}".format(float(tip)) + " tip split " + str(split) + " ways = ${:,.2f}".format(float(tip_split)) ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                self.ids.list_of_steps.add_widget(Label(text= "Each person's total = ${:,.2f}".format(float(total_split)) ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
            else:
                print("Invalid Input")
                self.ids.list_of_steps.add_widget(Label(text= "" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            
        except Exception:
            try:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                    
            except Exception:               
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)        

#Derivatives Calculator
Builder.load_string("""
<Derivatives>
    id:Derivatives
    name:"Derivatives"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Derivatives Calculator"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        prime.text = ""
                        respect.text = ""
                        value.text = ""
                        list_of_steps.clear_widgets()       
        
            TextInput:
                id: entry
                text: entry.text
                hint_text: "f(x)="
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10              
            
            TextInput:
                id: prime
                text: prime.text
                hint_text: "# of times to derive"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10            
                input_filter: lambda text, from_undo: text[:2 - len(prime.text)]
                
            TextInput:
                id: respect
                text: respect.text
                hint_text: "With respect to: x, y or z"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10  
                input_filter: lambda text, from_undo: text[:1 - len(respect.text)]
                
            TextInput:
                id: value
                text: value.text
                hint_text: "Respect = Value"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10  
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Derivative"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()
                        Derivatives.derive(entry.text + "&" + prime.text + "$" + respect.text + "%" + value.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

#Integration Calculator
Builder.load_string("""
<Integration>
    id:Integration
    name:"Integration"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Integration Calculator"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        prime.text = ""
                        respect.text = ""
                        value.text = ""
                        list_of_steps.clear_widgets()       
        
            TextInput:
                id: entry
                text: entry.text
                hint_text: "f(x)="
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10              
            
            TextInput:
                id: prime
                text: prime.text
                hint_text: "# of times to integrate"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10              
                input_filter: lambda text, from_undo: text[:2 - len(prime.text)]
                
            TextInput:
                id: respect
                text: respect.text
                hint_text: "With respect to: x, y or z"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10  
                input_filter: lambda text, from_undo: text[:1 - len(respect.text)]
                
            TextInput:
                id: value
                text: value.text
                hint_text: "Definite Integral: a,b"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10  
                
                    
            Button:
                id: steps
                text: "Integrate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1, 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets()
                    Integration.Integrate(entry.text + "&" + prime.text + "$" + respect.text + "%" + value.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")


#Limits
Builder.load_string("""
<Limits>
    id:Limits
    name:"Limits"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Limits Calculator"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        range.text = ""
                        direction.text = ""
                        list_of_steps.clear_widgets()       
        
            TextInput:
                id: entry
                text: entry.text
                hint_text: "lim:"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10              
            
            TextInput:
                id: range
                text: range.text
                hint_text: "x -> n:"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                
            TextInput:
                id: direction
                text: direction.text
                hint_text: "direction: + or -"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                input_filter: lambda text, from_undo: text[:1 - len(direction.text)]
            
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    text: "\u221E"  
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 1, 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release: 
                        range.text = "\u221E"
                        
                Button:
                    text: "-\u221E"  
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 1, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release: 
                        range.text = "-\u221E"
                    
            Button:
                id: steps
                text: "Limit"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1, 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets()
                    Limits.Limit(entry.text + "&" + range.text + "%" + direction.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Derivatives(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Derivatives, self).__init__(**kwargs)
        
    layouts = []
    def derive(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("~~~~~~~~~~~~~~~~~~~~")
        print("DERIVATE")
        
        try:
            print("Entry",entry)
            amp = entry.find("&")
            dollar = entry.find("$")
            percent_sign = entry.find("%")
            
            func = entry[:amp]
            print("func",func)       
            
            prime = entry[amp+1:dollar]
            print("Prime:",prime)
            if prime == "":
                prime = 0
            
            respect = entry[dollar + 1:percent_sign]
            print("respect:",respect)
            
            value = entry[percent_sign+1:]
            print("value:",value)
            if value == "":
                value = "Nothing"
            
            if respect == "x":
                respect = Symbol(respect)
                print("Respect officially:",respect)
            elif respect == "y":
                respect = Symbol(respect)
                print("Respect officially:",respect)
            elif respect == "z":
                respect = Symbol(respect)
                print("Respect officially:",respect)
            else:
                print("Invalid Respect Input" )
            
            if int(prime) > 0 and str(respect) != "":
                self.ids.list_of_steps.add_widget(Label(text= "f(" + str(respect) + ") = " + str(func).replace("**","^").replace("*x","x").replace("*y","y").replace("*z","z").replace("+"," + ").replace("-"," - ").replace("***","**") ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Derive " + str(prime) + " time(s) with respect to " + str(respect),font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                print("_________________________________________")
                
                i = 0 #     2sin(2x)^2+3x^3+e^x-2ln(3x)
                while i < int(prime):
                    
                    print("Starting",i+1,"derivative")
                    func = func.replace("**","^").replace("*","")
                    print("func:",func)
                    func = str(func).replace(" ","").replace("^","**").replace("x","*x").replace("y","*y").replace("z","*z")
                    func = func.replace("-*x","-1*x").replace("-*y","-1*y").replace("-*z","-1*z")
                    func = func.replace("+*x","+1*x").replace("+*y","+1*y").replace("+*z","+1*z")
                    func = func.replace("(*x","(1*x").replace("(*y","(1*y").replace("(*z","(1*z")
                    func = func.replace("(-*x","(-1*x").replace("(-*y","(-1*y").replace("(-*z","(-1*z")
                    func = func.replace("sin","*sin").replace("cos","*cos").replace("tan","*tan").replace("sec","*sec").replace("csc","*csc").replace("cot","*cot")
                    func = func.replace("ln","*ln").replace("log","*log")
                    func = func.replace("e**","*e**").replace("(*e**","(e**")
                    func = func.replace("+-","-").replace("-+","-")
                    func = func.replace("-*","-1*").replace("+*","+1*").replace("/*","/")
                    func = func.replace("***","**").replace("(*","(")
                    print("func filtered:",func)
                    
                    if func[0] == "*":
                        func = "1" + func
                        print("func fixed, * = [0]:",func)
                    print("func = ",func)
                    print("func data type",type(func))

                    func = str(diff(func,str(respect)))
                    print("Answer:",func)

                    print()
                    func_display_list = str(func).strip().split(" ")
                    print("func_display_list",func_display_list)
                    
                    if len(func_display_list) > 5 and len(func_display_list) < 12:
                        print("IF")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        func_display_front_slice = str(func_display_list[:5]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_front_slice",func_display_front_slice)
                        
                        func_display_back_slice = str(func_display_list[5:]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_back_slice",func_display_back_slice)
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * (i+1) + "(" + str(respect) + ") = " + str(func_display_front_slice).replace("**","^"),font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_back_slice).replace("**","^") ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                    elif len(func_display_list) > 12:
                        print("ELIF")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        func_display_front_slice = str(func_display_list[:5]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_front_slice",func_display_front_slice)
                        
                        func_display_mid_slice = str(func_display_list[5:11]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_mid_slice",func_display_mid_slice)
                        
                        func_display_back_slice = str(func_display_list[11:]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_back_slice",func_display_back_slice)
                        
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * (i+1) + "(" + str(respect) + ") = " + str(func_display_front_slice).replace("**","^") ,font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_mid_slice).replace("**","^"),font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_back_slice).replace("**","^") ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                    else:
                        print("ELSE")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("func_display_list",func_display_list)
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * (i+1) + "(" + str(respect) + ") = " + str(func).replace("**","^"),font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
                    print("Completed",i+1,"derivative")
                    print("_________________________________________")
                    i = i + 1
                    
            if value != "Nothing":
                print("func = ",func)
                
                func = str(func).replace(str(respect),str(value)).replace("sqrt","math.sqrt").replace("pi","math.pi").replace("^","**").replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan").replace("csc","math.csc").replace("sec","math.sec").replace("cot","math.cot").replace("log","math.log").replace("e","math.e").replace("smath.ec","math.sec").replace("math.smath.secc","math.sec")
                print("func replaced x = ",func)
                
                func_evaled = eval(str(func))
                print("func_evaled = ",func_evaled)
                
                self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * (i) + "(" + value + ") = " + str(func_evaled),font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            else:
                if int(prime) == 0:
                    self.ids.list_of_steps.add_widget(Label(text= "Prime must be greater than 0!" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif str(respect) == "":
                    self.ids.list_of_steps.add_widget(Label(text= "Respect must be entered" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
class Integration(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Integration, self).__init__(**kwargs)
                
    layouts = []
    def Integrate(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("~~~~~~~~~~~~~~~~~~~~")
        print("INTEGRATE")
        
        try:
            print("Entry",entry)
            amp = entry.find("&")
            dollar = entry.find("$")
            percent_sign = entry.find("%")
            
            func = entry[:amp]
            print("func",func)       
            
            prime = entry[amp+1:dollar]
            print("Prime:",prime)
            if prime == "":
                prime = 0
            
            respect = entry[dollar + 1:percent_sign]
            print("respect:",respect)
            
            value = entry[percent_sign+1:]
            print("value:",value)
            if value == "":
                value = "Nothing"
            if value.count(",") == 1:
                comma = value.find(",")
                a = value[:comma]
                print("a = ",a)
                
                b = value[comma+1:]
                print("b = ",b)
            
            x = sym.Symbol("x")
            y = sym.Symbol("y")
            z = sym.Symbol("z")
            
            if int(prime) > 0 and str(respect) != "":
                self.ids.list_of_steps.add_widget(Label(text= "f(" + respect + ") = " + str(func).replace("**","^").replace("*x","x").replace("*y","y").replace("*z","z").replace("-"," - ").replace("+"," + ").replace("***","**") ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Integrate " + str(prime) + " time(s) with respect to " + str(respect),font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                print("_________________________________________")
                
                func = func.replace(" ","").replace("+"," + ").replace("-"," - ").replace("^ -","^-").replace("^ +","^+")
                print("func",func)
                
                k = 0
                while k < int(prime):
                    if func.count("(") > 0 and func.count(")") > 0:
                        if func.count("(") == func.count(")"):
                            print("Parenthesis Found")
                            i = 0
                            while i < len(func):
                                if func[i] == ")":
                                    right_par_index = i
                                    print("right_par_index",right_par_index)
                                    left_par_index = func[:i].rfind("(")
                                    print("left_par_index",left_par_index)
                                    range_pars = func[left_par_index:right_par_index+1]
                                    print(range_pars)
                                    cleaned = range_pars.replace(" ","")
                                    print("cleaned",cleaned)
                                    func = func[:left_par_index] + cleaned + func[right_par_index+1:] 
                                    print("func cleaned",func)
                                    print()
                                i = i + 1 
                                
                        else:
                            print("Parentheses Unbalanced!")
                    
                    func_list = func.strip().split(" ")
                    print()
                    print("func_list",func_list)
                    print()
                    
                    #If + or - is first element in list
                    new_func_list = []
                    if func_list[0] == "+" or func_list[0] == "-":
                        print("IF")
                        i = 0
                        while i < len(func_list):
                            if func_list[i] == "+" or func_list[i] == "-":
                                new_func_list.append(func_list[i] + func_list[i+1])
                            i = i + 1
                        print("new_func_list",new_func_list)
                    #If + or - is second element in list    
                    elif len(func_list) > 1:
                        if func_list[1] == "+" or func_list[1] == "-":
                           print("ELIF")
                           i = 0
                           while i < len(func_list):
                               if func_list[i] == "+" or func_list[i] == "-":
                                   new_func_list.append(func_list[i] + func_list[i+1])
                               i = i + 1
                           print("new_func_list:",new_func_list)
                           new_func_list = [func_list[0]] + new_func_list
                           print("new_func_list",new_func_list)
                        
                    #If + or - is not apart of list
                    else:
                        print("ELSE")
                        new_func_list.append(func_list[0])
                        print("new_func_list",new_func_list)
                        
                    print()
                    print("integrate each element and store in empty list")
                    print()
                    
                    i = 0
                    while i < len(new_func_list):
                        #finding e
                        if new_func_list[i].count("e") > 0 and new_func_list[i].count("s") == 0 and new_func_list[i].count("c") == 0 and new_func_list[i].count("t") == 0:
                            print()
                            print("Found e")
                            carrot_index = new_func_list[i].find("^")
                            print("carrot_index: ",carrot_index)
                            exponent_range = new_func_list[i][carrot_index+1:]
                            print("exponent_range:",exponent_range)
                            if exponent_range[0] == "x" or exponent_range[0] == "y" or exponent_range[0] == "z":
                                exponent_range = "1" + exponent_range
                                print("e^x fixed: ",exponent_range)
                                new_func_list[i] = new_func_list[i][:carrot_index] + "^" + exponent_range
                                print("new_func_list[i]:",new_func_list[i])
                                if new_func_list[i][0] == "*":
                                    new_func_list[i] = new_func_list[i][1:]
                                    print("found stray *")
                                    print("Cleaned:",new_func_list[i])
                            else:
                                print("e element okay for integration: ",new_func_list[i])
                                if new_func_list[i][0] == "*":
                                    new_func_list[i] = new_func_list[i][1:]
                                    print("found stray *")
                                    print("Cleaned:",new_func_list[i])
                        #finding all other elements
                        else:
                            print()
                            print("Found non-e element:",new_func_list[i])
                            if new_func_list[i][0] == "*":
                                new_func_list[i] = new_func_list[i][1:]
                                print("found stray *")
                                print("Cleaned:",new_func_list[i])
                            
                        i = i + 1
                        
                    print()
                    print("new_func_list with fixed e elements: ",new_func_list)
                    print()
                    
                    answer_integrated = []
                    #While loop to clean each element
                    i = 0
                    while i < len(new_func_list):
                        print("Cleaning ",new_func_list[i])
                        new_func_list[i] = new_func_list[i].replace("^","**").replace("x","*x").replace("y","*y").replace("z","*z")
                        new_func_list[i] = new_func_list[i].replace("sin","*sin").replace("cos","*cos").replace("tan","*tan").replace("sec","*sec").replace("csc","*csc").replace("cot","*cot")
                        new_func_list[i] = new_func_list[i].replace("e**","*e**").replace("(*e**","(e**").replace("-*","-").replace("+*","+").replace("(*x","(x").replace("(*y","(y").replace("(*z","(z").replace("(*","(")
                        print("new_func_list[i]: ",new_func_list[i])
                        
                        if new_func_list[i][0] == "*":
                            new_func_list[i] = new_func_list[i][1:]
                            print("found stray *")
                            print("Cleaned:",new_func_list[i])
                        
                        print()
                        i = i + 1
                        
                    print()
                    print("new_func_list with cleaned elements: ",new_func_list)
                    print()
                        
                    #Concat all cleaned elements and integrate
                    #OR while loop to integrate each element and then concat
                    
                    func_concat = str(new_func_list).replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","").replace("+"," + ").replace("-"," - ")
                    print("func_concat: ",func_concat)
                    print()
                    if respect == "x":
                        print("Integrating with respect to X")
                        func_integrated = str(sym.integrate(str(func_concat),x)).replace("**","^")
                        print("func_integrated",func_integrated)
                    elif respect == "y":
                        print("Integrating with respect to Y")
                        func_integrated = str(sym.integrate(str(func_concat),y)).replace("**","^")
                        print("func_integrated",func_integrated)
                    elif respect == "z":
                        print("Integrating with respect to Z")
                        func_integrated = str(sym.integrate(str(func_concat),z)).replace("**","^")
                        print("func_integrated",func_integrated)
                    
                    func_integrated_list = func_integrated.split(" ")
                    print("func_integrated_list",func_integrated_list)
                    
                    func_integrated_list_empty = []
                    j = 0
                    while j < len(func_integrated_list):
                        if func_integrated_list != "+" or func_integrated_list != "-":
                            print("found non +-")
                            if func_integrated_list[j].count("/") > 0:
                                print("if")
                                div_sign_index = func_integrated_list[j].find("/")
                                print("div_sign_index",div_sign_index)
                                func_integrated_list_to_append = "(" + func_integrated_list[j][:div_sign_index] + ")" + func_integrated_list[j][div_sign_index:]
                                print("func_integrated_list_to_append",func_integrated_list_to_append)
                                func_integrated_list_empty.append(func_integrated_list_to_append)
                            else:
                                print("else")
                                func_integrated_list_empty.append(func_integrated_list[j])
                        else:
                            func_integrated_list_empty.append(func_integrated_list[j])
                        j = j + 1
                    print("func_integrated_list_empty",func_integrated_list_empty)
                        
                            
                    if len(func_integrated_list_empty) > 5:
                        func_integrated_list_empty_to_five = str(func_integrated_list_empty[:5]).replace("[","").replace("]","").replace(",","").replace("'","")
                        print("func_integrated_list_empty_to_five",func_integrated_list_empty_to_five)
                        
                        func_integrated_list_empty_five_out = str(func_integrated_list_empty[5:]).replace("[","").replace("]","").replace(",","").replace("'","")
                        print("func_integrated_list_empty_five_out",func_integrated_list_empty_five_out)
                    
                        self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "∫" * (k+1) + "f" + "(" + respect + ") = " + func_integrated_list_empty_to_five,font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= func_integrated_list_empty_five_out,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
                    else:
                        func_integrated_list_empty = str(func_integrated_list_empty[:]).replace("[","").replace("]","").replace(",","").replace("'","")
                        self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "∫" * (k+1) + "f" + "(" + respect + ") = " + func_integrated_list_empty,font_size = '15sp', size_hint_y= None, height=100))

                    
                    func = func_integrated.replace("**","^").replace("*","")
                    print("func ready for next loop, func = ",func_integrated)
                    print()
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    k = k + 1
                    
            if value != "Nothing":
                print("func = ",func_integrated)
                
                func_a = str(func_integrated).replace(respect,a).replace("sqrt","*math.sqrt").replace("pi","*math.pi").replace("^","**").replace("sin","*math.sin").replace("cos","*math.cos").replace("tan","*math.tan").replace("csc","*math.csc").replace("sec","*math.sec").replace("cot","*math.cot").replace("log","*math.log").replace("e","*math.e").replace("smath.ec","*math.sec").replace("math.smath.secc","*math.sec").replace("-*","-").replace(" *m"," m").replace("(*m","(m")
                print("func_a replaced respect = ",func_a)
                
                if func_a[:2] == "*m":
                    func_a = func_a[1:]
                    print("func_a cleaned front",func_a)
                
                func_a_evaled = eval(str(func_a))
                print("func_a_evaled = ",func_a_evaled)
                
                self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "∫f" + "(" + a + ") = " + "{:,.2f}".format(float(str(func_a_evaled))),font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                func_b = str(func_integrated).replace(respect,b).replace("sqrt","*math.sqrt").replace("pi","*math.pi").replace("^","**").replace("sin","*math.sin").replace("cos","*math.cos").replace("tan","*math.tan").replace("csc","*math.csc").replace("sec","*math.sec").replace("cot","*math.cot").replace("log","*math.log").replace("e","*math.e").replace("smath.ec","*math.sec").replace("math.smath.secc","*math.sec").replace("-*","-").replace(" *m"," m").replace("(*m","(m")
                print("func_b replaced respect = ",func_b)
                
                if func_b[:2] == "*m":
                    func_b = func_b[1:]
                    print("func_b cleaned front",func_b)
                
                func_b_evaled = eval(str(func_b))
                print("func_b_evaled = ",func_b_evaled)

                self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "∫f" + "(" + b + ") = " + "{:,.2f}".format(float(str(func_b_evaled))),font_size = '15sp', size_hint_y= None, height=100))
                
                a = str(eval(a.replace("sqrt","math.sqrt").replace("pi","math.pi").replace("ln","math.log").replace("log","math.log").replace("e","math.e").replace("^","**")))
                    
                b = str(eval(b.replace("sqrt","math.sqrt").replace("pi","math.pi").replace("ln","math.log").replace("log","math.log").replace("e","math.e").replace("^","**")))
                
                print("a = ",a)
                print("b = ",b)
                
                if float(a) < float(b):
                    self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "∫f" + "(" + b + ") - " + "∫f" + "(" + a + ") =",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "{:,.2f}".format(float(str(func_b_evaled))) + " - " + "{:,.2f}".format(float(str(func_a_evaled))) + " =",font_size = '15sp', size_hint_y= None, height=100))
                    
                    integral_evaled = str(float(func_b_evaled) - float(func_a_evaled))
                    print("integral_evaled",integral_evaled)
 
                    self.ids.list_of_steps.add_widget(Label(text= "{:,.2f}".format(float(integral_evaled)),font_size = '15sp', size_hint_y= None, height=100))

                
                else:
                    self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "b must be greater than a!" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
            else:
                if int(prime) == 0:
                    self.ids.list_of_steps.add_widget(Label(text= "Prime must be greater than 0!" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif respect == "":
                    self.ids.list_of_steps.add_widget(Label(text= "Respect must be entered" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)        


class Limits(Screen):
    sm = ScreenManager()
    
    def __init__(self, **kwargs):
        super(Limits, self).__init__(**kwargs)
            
    layouts = []
    def Limit(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("~~~~~~~~~~~~~~~~~~~~")
        print("LIMIT")
        
        try:
            print()
            print("Entry",entry)
            
            amp = entry.find("&")
            
            perc = entry.find("%")
            
            func = entry[:amp]
            print("func: ",func)
            
            func = func.replace("^","**").replace("x","*x").replace("***","**")
            func = func.replace("sin","*sin").replace("cos","*cos").replace("tan","*tan").replace("sec","*sec").replace("csc","*csc").replace("cot","*cot")
            func = func.replace("e","*e").replace("s*ec","sec").replace("-*","-").replace("+*","+").replace("(*x","(x").replace("(*y","(y").replace("(*z","(z").replace("/*","/")
            print("func cleaned: ",func)
            
            if func[0] == "*":
                func = func[1:]
                print("func cleaned: ",func)
            
            limit = entry[amp+1:perc]
            print("limit: ",limit)
            
            direction = entry[perc+1:]
            print("direction",direction)
            
            if limit == "∞":
                print("TO + INFINITY AND BEYONDDDD")
                limit = S.Infinity
                print("Limit: ",limit)
                print("func: ",func)
                x = Symbol("x")
                
                L = Limit(func,x,limit,dir=str(direction))
                
                Answer = str(L.doit()).replace("AccumBounds","Range : ")
                
                print()
                print("Answer: ",Answer)
            elif limit == "-∞":
                print("TO - INFINITY AND BEYONDDDD")
                limit = S.NegativeInfinity
                print("Limit: ",limit)
                print("func: ",func)
                
                x = Symbol("x")
                L = Limit(func,x,limit,dir=direction)
                Answer = str(L.doit()).replace("AccumBounds","Range : ")
                print()
                print("Answer: ",Answer)
                
            else:
                print("func: ",func)
                x = Symbol("x")
                L = Limit(func,x,limit,dir=direction)
                Answer = str(L.doit()).replace("AccumBounds","Range : ")
                print()
                print("Answer: ",Answer)
                
                
            self.ids.list_of_steps.add_widget(Label(text= "The Limit of :" ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "Lim (x -> " + str(limit) + ") " + direction + " : " + str(func).replace("**","^") ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "=" ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= str(Answer).replace("**","^") ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
#Domain and Range Calculator 
Builder.load_string("""
<Domain_and_Range>
    id:Domain_and_Range
    name:"Domain_and_Range"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Domain and Range"
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        y.text = ""
                        domain.text = ""
                        list_of_steps.clear_widgets()            
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "f(x) = ax + b"       
                                                        
            TextInput:
                id: y
                text: y.text
                multiline: False
                hint_text: "f(x) ="
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10
                    
            TextInput:
                id: domain
                text: domain.text
                multiline: False
                hint_text:"Domain = min,max,sequence"
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10  
                
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Domain_and_Range.steps(y.text + "&" + domain.text)  
                
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

class Domain_and_Range(Screen):
    sm = ScreenManager()
    
    def __init__(self, **kwargs):
        super(Domain_and_Range, self).__init__(**kwargs)
                
    layouts = []
    def steps(self,entry):
        print()
        print("~~~~~~~~~~~~~~~~")
        print("entry:",entry)
        entry.replace(" ","")
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print()
            amp = entry.find("&")
            y = entry[:amp]
            print("y:",y)
            
            self.ids.list_of_steps.add_widget(Label(text= "y = " + y.replace(" ","").replace("y=","").replace("+"," + ").replace("-"," - ") ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            domain = entry[amp+1:]
            print("domain",domain)
            
            domain_comma = domain.find(",")
            comma_count = domain.count(",")
            
            print("domain_comma",domain_comma)
            
            if comma_count == 0 and y.count("x") > 0:
                y = y.replace("x","*" + str(domain)).replace("+*","+").replace("-*","-").replace("/*","/").replace("(*","(").replace("(*","(").replace("sqrt","math.sqrt").replace("pi","math.pi").replace("^","**").replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan").replace("csc","mpmath.csc").replace("sec","mpmath.sec").replace("cot","mpmath.cot").replace("log","math.log").replace("e","math.e").replace("smath.ec","mp.sec").replace("math.smath.secc","mp.sec").replace("math.math","math").replace("mp.mp","mp")
                print("y = ",y)
                if y[0] == "*":
                    y = y.replace("*","")
                y = y.replace("^","**")
                y = str(eval(y))
                
                self.ids.list_of_steps.add_widget(Label(text= "Domain | Range" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "x | y" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(domain) + " | " + str(y) ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            elif comma_count == 1 and y.count("x") > 0:
                
                empty_domain = []
                for x in range(int(domain[:domain_comma]), int(domain[domain_comma + 1:]) + 1):
                	empty_domain.append(x)
                print("empty_domain",empty_domain) 
                
                i = 0
                range_y = []
                print("loop start")
                print(len(empty_domain))
                
                self.ids.list_of_steps.add_widget(Label(text= "Domain | Range" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "x | y" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                while i < len(empty_domain):
                    y_input = str(y).replace("x","*" + str(empty_domain[i])).replace("+*","+").replace("-*","-").replace("/*","/").replace("(*","(").replace("sqrt","math.sqrt").replace("pi","math.pi").replace("^","**").replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan").replace("csc","mpmath.csc").replace("sec","mpmath.sec").replace("cot","mpmath.cot").replace("log","math.log").replace("e","math.e").replace("smath.ec","mp.sec").replace("math.smath.secc","mp.sec").replace("math.math","math").replace("mp.mp","mp")
                    if y_input[0] == "*":
                        y_input = y_input.replace("*"," ")
                    print("y_input",y_input)
                    y_input = y_input.replace("^","**")
                    y_solved = eval(y_input)
                    print("y_solved",y_solved)
                    range_y.append(y_solved)
                    
                    self.ids.list_of_steps.add_widget(Label(text= str(empty_domain[i]) + " | " + str(y_solved) ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    i = i + 1
                    
                print("range_y",range_y)
                    
            elif comma_count == 2 and y.count("x") > 0:
                print("domain",domain)
                
                domain_list = str(domain).split(",")
                print(domain_list)
                
                sequence_list = []
                for x in range(int(domain_list[0]),int(domain_list[1]),int(domain_list[2])):
                    sequence_list.append(x)
                print("sequence_list",sequence_list)    
                
                if y.count("x") > 0:
                    i = 0
                    range_y = []
                    print("loop start")
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Domain | Range" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "x | y" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    while i < len(sequence_list):
                        y_input = str(y).replace("x","*" + str(sequence_list[i])).replace("+*","+").replace("-*","-").replace("/*","/").replace("(*","(").replace("sqrt","math.sqrt").replace("pi","math.pi").replace("^","**").replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan").replace("csc","mpmath.csc").replace("sec","mpmath.sec").replace("cot","mpmath.cot").replace("log","math.log").replace("e","math.e").replace("smath.ec","mp.sec").replace("math.smath.secc","mp.sec").replace("math.math","math").replace("mp.mp","mp")
                        if y_input[0] == "*":
                            y_input = y_input.replace("*","")
                        print("y_input",y_input)
                        y_input = y_input.replace("^","**")
                        y_solved = eval(y_input)
                        print("y_solved",y_solved)
                        range_y.append(y_solved)
                        
                        self.ids.list_of_steps.add_widget(Label(text= str(sequence_list[i]) + " | " + str(y_solved) ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
                        i = i + 1
                        
                    print("range_y",range_y)
                    
                else:
                    self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))     
sm.add_widget(Basic(name="Basic"))     
sm.add_widget(Exponents_steps(name="Exponents_steps")) #Line 186, individual app and apart of bundle
sm.add_widget(Percentage_Calculator(name="Percentage_Calculator"))  #Line 379, individual app and apart of bundle
sm.add_widget(PEMDAS(name="PEMDAS")) #Line 573 ,individual app and apart of bundle
sm.add_widget(Fractions(name="Fractions")) #1101 ,individual app and apart of bundle
sm.add_widget(Pythagorean(name="Pythagorean"))    #Line 2996, individual app and apart of bundle
sm.add_widget(Quadratic_Formula_Solver(name="Quadratic_Formula_Solver")) #Line 3183, individual app and apart of bundle
sm.add_widget(Fractions_converter(name="Fractions_converter")) #individual app and apart of bundle
sm.add_widget(Decimals_converter(name="Decimals_converter"))     #individual app and apart of bundle
sm.add_widget(Percentages_converter(name="Percentages_converter"))#individual app and apart of bundle
sm.add_widget(Statistical_Calculator(name="Statistical_Calculator")) #Line 4315
sm.add_widget(FOIL(name="FOIL")) #4677, individual app and apart of bundle 
sm.add_widget(Tip_Calculator(name="Tip_Calculator"))    #Line 5544, individual app and apart of bundle 
sm.add_widget(Derivatives(name="Derivatives"))     #Line 5772, individual app and apart of bundle 
sm.add_widget(Integration(name="Integration"))
sm.add_widget(Limits(name="Limits"))
sm.add_widget(Domain_and_Range(name="Domain_and_Range")) #7401
sm.add_widget(updates(name="updates"))
sm.current = "Homepage"   
print("Current Page:",sm.current)

class Bundled(App):
    
    def __init__(self, **kwargs):
        super(Bundled, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm

if __name__ == '__main__':
    Bundled().run()
    
