## Emerging Systems Architectures & Technologies
Raspberry Pi Project Artifact & Reflection
Selected Artifact
For this portfolio submission, I have selected my Raspberry Pi GPIO Control Project, which best demonstrates my ability to write interface software that communicates directly with hardware components. This project highlights my understanding of embedded systems, hardware-software interaction, and performance considerations in emerging system architectures.

Project Reflection
Summarize the project and what problem it was solving.
The Raspberry Pi GPIO Control Project was designed to interface with physical hardware components—such as LEDs, sensors, or motors—through the GPIO (General Purpose Input/Output) pins of a Raspberry Pi. The goal was to demonstrate how low-cost embedded systems can be used to control and monitor physical environments. It solved the challenge of integrating software with real-world hardware, enabling real-time control and feedback through Python scripts.

### _What did you do particularly well?_
I successfully implemented GPIO control using Python, ensuring the code was modular, well-commented, and easy to understand. I paid close attention to GPIO pin configuration, circuit safety, and error handling, which made the project reliable and robust. I also integrated logic that allowed hardware components to respond dynamically to input, such as turning on an LED when a sensor detected motion or a button was pressed.

### _Where could you improve?_
While the project functioned well, I could improve by expanding the application to support asynchronous events or multitasking, using threading or interrupts for more efficient sensor polling. Additionally, adding a GUI or web-based interface would enhance user interaction and accessibility.

### _What tools and/or resources are you adding to your support network?_
Throughout the project, I added several valuable tools and resources to my support network:

The RPi.GPIO and gpiozero Python libraries for simplified GPIO interaction

The Raspberry Pi Documentation and online forums such as the Raspberry Pi Stack Exchange

Physical tools like a breadboard, jumper wires, and various sensors/LEDs for prototyping

These tools will remain essential as I continue working with embedded systems and IoT devices.

### _What skills from this project will be particularly transferable to other projects and/or coursework?_
This project helped strengthen my skills in:

Hardware-software integration

Python scripting for embedded systems

Circuit design and GPIO control

Debugging real-time input/output systems

These are highly transferable to any future IoT, robotics, or embedded computing projects, as well as in professional environments where low-level hardware interaction is critical.

### _How did you make this project maintainable, readable, and adaptable?_
I structured the code using functions for each hardware task, used descriptive variable names, and included clear documentation on how to set up the hardware connections. The project was designed so that additional components (e.g., new sensors or actuators) could be added with minimal changes to the existing code. Additionally, I included safety checks to prevent GPIO pin conflicts and potential hardware damage, making the solution safe and adaptable.
