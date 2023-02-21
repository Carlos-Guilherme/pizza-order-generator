# pizza-order-generator
This is a Python program that uses a custom library called customtkinter to create a graphical user interface (GUI). The GUI consists of a main window with a frame that contains two tabs (tabs): "Create order" and "Assemble from scratch".

In the "Create order" tab, there is another frame with two tabs: "Assemble from scratch" and "Ready flavors". The "Ready flavors" tab contains three radio options for selecting pizza flavors ("4 Cheeses", "Calabresa" and "Chicken catupery"), a "Generate order" button and a text field for displaying the generated order .

The "Build from Scratch" tab contains two frames, one for edge selection and one for sauce selection. Both frames contain radio options for selection.

By selecting the required options and clicking the "Generate Order" button on the "Ready Flavors" tab, the program generates an order number and displays the complete order in the text field on the same tab. The text field is set to read-only after the order is displayed.

The program also imports the pyperclip library, which is used to copy the request text to the operating system's clipboard.

For example, when creating an order in the "assemble from scratch" tab, we must select the options we want and then click on "generate order":

![image](https://user-images.githubusercontent.com/72580077/220379836-5fc2b618-5072-4104-9f39-b1eb037b09c9.png)

After the request is stopped and remains in the "order scripts" tab

![image](https://user-images.githubusercontent.com/72580077/220380268-c656c21f-9a8d-441f-8dce-153f97daeda0.png)

Just below we have two buttons, one to copy the order and another to clean the output
