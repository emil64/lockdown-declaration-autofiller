# Lockdown declaration filler

dependencies:

* ``` pdfwr``` . You can install it by typing ```pip3 install pdfwr``` in the terminal.

## Preparation

You may need to do some preparation:

* open ```data/persons.json``` in your favourite text editor to add persons. The format is ```"fiel_key" : "field_value"```.  You will also need to add a username and a path to the signature (which must be saved in pdf format). Fields with the value ```$date``` will be automatically replaced with the current date. Here is and example:

  ```json
  {
    "people" : [
      {
        "username" : "username",
        "nume": "Second Name",
        "prenume": "First Name",
        "ziua" : "Day",
        "luna" : "Month",
        "anul" : "Year",
        "fill_8" : "Address line 1",
        "fill_9" : "Address line 2",
        "fill_1" : "$date",
        "signature": "sign.pdf"
      }
    ]
  }
  ```



 * the same goes for ```data/activities.json```. You will need to add a ```name``` field. Here is an example of ```activities.json```

   ```json
   {
     "reasons" : [
       {
         "activity" : "runnning",
         "fill_10": "Clifton Bridge",
         "Check Box5": "/YES",
         "Check Box2": "/YES"
       }
     ]
   }
   ```

* the signature has to be placed in ```data/signatures```. For best results its height should be around 88px. Otherwise, you might want to tweak its coordinates in ```fill.py```, lines 34 and 35.



## Running

Run it by typing ```python3 fill.py username activity``` in the terminal, replacing username and activity with the ones you want from the json files.



The code was specifically made to work with the Romanian declaration, but feel free to edit it for other forms.

#### Take care and stay home!

