1. File generator

The file generator tech test comes with a mock data CSV that represents one of the many types of data that we have to deal with at Morrisons.

The challenge is to consume and transform the CSV file in to a nested JSON file which will form a tree structure.

2. How to Generate the desired Structure

Run the tree.py file using the command "python tree.py" and after running the file the desired tree structure will be stored in data.json file. The tree.py file consists of three functions , as mentioned below.

        A. Main() is responsible for opening the csv file and looping each and every row of the csv file and after completion the looping and structuring 
        the desired tree it will store the JSON object into json file and as here I use context managers (WITH) therefor no chance to loosing resource(Here CSV File).
        B. createLeaf() is responsible for creating parent node and it's child node recursively and genearates the desired tree structure.
        C. createTree() is responsible for generating the default dictionary.

3. Prerequisites

Only python need to be installed into the System.

4. Expected Output after running the file (tree.py)



[
 {
  "Base URL": "https://groceries.morrisons.com/browse",
  "children": [
   {
    "label": "THE BEST",
    "id": "178974",
    "link": "https://groceries.morrisons.com/browse/178974",
    "children": [
     {
      "label": "FRESH",
      "id": "178969",
      "link": "https://groceries.morrisons.com/browse/178974/178969",
      "children": [
       {
        "label": "CHEESE",
        "id": "178975",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178975"
       },
       {
        "label": "COOKED MEAT & ANTIPASTI",
        "id": "178976",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178976"
       },
       {
        "label": "DAIRY & EGGS",
        "id": "178977",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178977"
       },
       {
        "label": "DESSERTS",
        "id": "178978",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178978"
       },
       {
        "label": "DRINKS",
        "id": "178979",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178979"
       },
       {
        "label": "FISH & SEAFOOD",
        "id": "178980",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178980"
       },
       {
        "label": "FRUIT & VEGETABLES",
        "id": "178981",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178981"
       },
       {
        "label": "MEAT & POULTRY",
        "id": "178982",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178982"
       },
       {
        "label": "NUTS & SNACKS",
        "id": "178983",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178983"
       },
       {
        "label": "PIES & QUICHES ",
        "id": "178984",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178984"
       },
       {
        "label": "PIZZA, PASTA & GARLIC BREAD",
        "id": "178985",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178985"
       },
       {
        "label": "READY MEALS",
        "id": "178986",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178986"
       },
       {
        "label": "SAVOURY SNACKS & CHILLED",
        "id": "178987",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178987"
       },
       {
        "label": "SOUPS & SAUCES",
        "id": "178988",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178988"
       },
       {
        "label": "VEGETARIAN",
        "id": "178989",
        "link": "https://groceries.morrisons.com/browse/178974/178969/178989"
       }
      ]
     },
     {
      "label": "FOOD CUPBOARD",
      "id": "178970",
      "link": "https://groceries.morrisons.com/browse/178974/178970",
      "children": [
       {
        "label": "ANTIPASTI",
        "id": "178990",
        "link": "https://groceries.morrisons.com/browse/178974/178970/178990"
       },
       {
        "label": "BISCUITS & CRACKERS",
        "id": "178991",
        "link": "https://groceries.morrisons.com/browse/178974/178970/178991"
       },
       {
        "label": "BREAKFAST CEREALS",
        "id": "178992",
        "link": "https://groceries.morrisons.com/browse/178974/178970/178992"
       },
       {
        "label": "CHOCOLATE & SWEETS",
        "id": "178993",
        "link": "https://groceries.morrisons.com/browse/178974/178970/178993"
       },
       {
        "label": "CONDIMENTS & DRESSINGS",
        "id": "178994",
        "link": "https://groceries.morrisons.com/browse/178974/178970/178994"
       },
       {
        "label": "CRISPS & SAVOURY SNACKS",
        "id": "178995",
        "link": "https://groceries.morrisons.com/browse/178974/178970/178995"
       },
       {
        "label": "HOMEBAKING",
        "id": "179016",
        "link": "https://groceries.morrisons.com/browse/178974/178970/179016"
       },
       {
        "label": "JAMS, SPREADS & CHUTNEYS",
        "id": "179017",
        "link": "https://groceries.morrisons.com/browse/178974/178970/179017"
       },
       {
        "label": "PASTA",
        "id": "179018",
        "link": "https://groceries.morrisons.com/browse/178974/178970/179018"
       },
       {
        "label": "PUDDINGS & DESSERTS",
        "id": "179019",
        "link": "https://groceries.morrisons.com/browse/178974/178970/179019"
       },
       {
        "label": "SAUCES, STOCKS & GRAVY",
        "id": "179020",
        "link": "https://groceries.morrisons.com/browse/178974/178970/179020"
       },
       {
        "label": "TEA & COFFEE",
        "id": "179021",
        "link": "https://groceries.morrisons.com/browse/178974/178970/179021"
       },
       {
        "label": "TINS & CANS",
        "id": "179022",
        "link": "https://groceries.morrisons.com/browse/178974/178970/179022"
       }
      ]
     },
     {
      "label": "BAKERY & CAKES",
      "id": "178971",
      "link": "https://groceries.morrisons.com/browse/178974/178971",
      "children": [
       {
        "label": "BREAD & BREAD ROLLS",
        "id": "179023",
        "link": "https://groceries.morrisons.com/browse/178974/178971/179023"
       },
       {
        "label": "CAKES, PIES & TARTS",
        "id": "179024",
        "link": "https://groceries.morrisons.com/browse/178974/178971/179024"
       },
       {
        "label": "CROISSANTS & BREAKFAST BAKERY",
        "id": "179025",
        "link": "https://groceries.morrisons.com/browse/178974/178971/179025"
       },
       {
        "label": "DESSERTS & PUDDINGS",
        "id": "179026",
        "link": "https://groceries.morrisons.com/browse/178974/178971/179026"
       },
       {
        "label": "FRUITED BREAD, SCONES & HOT CROSS BUNS",
        "id": "179027",
        "link": "https://groceries.morrisons.com/browse/178974/178971/179027"
       }
      ]
     },
     {
      "label": "FROZEN",
      "id": "178972",
      "link": "https://groceries.morrisons.com/browse/178974/178972",
      "children": [
       {
        "label": "CAKES, PIES & TARTS",
        "id": "179028",
        "link": "https://groceries.morrisons.com/browse/178974/178972/179028"
       },
       {
        "label": "CHIPS, POTATOES & VEGETABLES",
        "id": "179029",
        "link": "https://groceries.morrisons.com/browse/178974/178972/179029"
       },
       {
        "label": "DESSERTS",
        "id": "179030",
        "link": "https://groceries.morrisons.com/browse/178974/178972/179030"
       },
       {
        "label": "FISH & SEAFOOD",
        "id": "179031",
        "link": "https://groceries.morrisons.com/browse/178974/178972/179031"
       },
       {
        "label": "ICE CREAM & LOLLIES",
        "id": "179032",
        "link": "https://groceries.morrisons.com/browse/178974/178972/179032"
       },
       {
        "label": "MEAT & POULTRY",
        "id": "179033",
        "link": "https://groceries.morrisons.com/browse/178974/178972/179033"
       },
       {
        "label": "PIES & PASTRIES",
        "id": "179034",
        "link": "https://groceries.morrisons.com/browse/178974/178972/179034"
       },
       {
        "label": "PIZZA & GARLIC BREAD",
        "id": "179035",
        "link": "https://groceries.morrisons.com/browse/178974/178972/179035"
       },
       {
        "label": "READY MEALS",
        "id": "179036",
        "link": "https://groceries.morrisons.com/browse/178974/178972/179036"
       }
      ]
     },
     {
      "label": "DRINKS",
      "id": "178973",
      "link": "https://groceries.morrisons.com/browse/178974/178973",
      "children": [
       {
        "label": "SOFT DRINKS",
        "id": "179037",
        "link": "https://groceries.morrisons.com/browse/178974/178973/179037"
       },
       {
        "label": "WINE & SPARKLING",
        "id": "179038",
        "link": "https://groceries.morrisons.com/browse/178974/178973/179038"
       },
       {
        "label": "BEER",
        "id": "179039",
        "link": "https://groceries.morrisons.com/browse/178974/178973/179039"
       }
      ]
     }
    ]
   }
  ]
 },
 {
  "Base URL": ""
 }
]
