<head>
    <meta http-equiv="Content-Type"content="text/html"charset="utf-8">
    <link href="./css_estilos/estilo_01.css"rel="stylesheet"type="text/css"> 
</head>

<div id='id0' > </div>

<body>
    <h1> <b> Mapp Reduce Approach to Stack Overflow Data Management </b> </h1>
</body>

<body>
    <h2> <b> Table of Contents </b> </h2>
</body>

1.  [<p style="font-family: rubik"> Project Scope Statement (Stack Overflow). </p>](#id1)
2.  [<p style="font-family: rubik"> The Issue. </p>](#id2)
3.  [<p style="font-family: rubik"> Methodological Approach. </p>](#id3)
4.  [<p style="font-family: rubik"> Tools and Technologies. </p>](#id4)
5.  [<p style="font-family: rubik"> Metadata Repository. </p>](#id5)
6.  [<p style="font-family: rubik"> How to Run. </p>](#id6)

---

<div id='id1' > </div>

<body>
    <h2> <b> Project Scope Statement (Stack Overflow) </b> </h2>
    <p>
    To access the project statement click here:
    </p>
</body>

[<p style="font-family: rubik"> Statement </p>](da_py_cases.pdf)

[<p style="font-family: rubik"> To Table of Contents </p> ](#id0)

---

<div id='id2' > </div>

<body>
    <h2> <b> The Issue </b> </h2>
    <p>
    To identify business's strengths and weaknesses, <b> Stack Overflow </b> needs to analyze the data recorded by the site over the last few years, through accurate comparisons and measurements.<br>
    <br>
    Being a voluminous dataset and written in .xml, it requires precise instructions to avoid redundancy in the processes and obtain accurate information on the attributes of interest, split the tasks into multiple processing threads, and save the outputs and logs opportunely. <br>
    <br>
    <h3> <b> Required Items </b> </h3>
    <ul>
        <li> Top 10 most viewed posts. </li>
        <li> Top 10 words by tag. </li>
        <li> Average response time. </li>
    </ul>
</body>

[<p style="font-family: rubik"> To Table of Contents </p> ](#id0)

---

<div id='id3' > </div>

<body>
    <h2> <b> Methodological Approach </b> </h2>
    <p>
    The map-reduce approach was adopted, based on the following steps: <br>
    <ol>
            <li> Identify, retrieve and store the attributes of interest, in a dictionary list type data structure with format: [{"key_atribute_1": "value_1"}, {"key_atribute_2": "value_2"}, ..., {"key_atribute_n": "value_n"}].  </p> </li>
            <li> Sort the list in ascending order.  </p> </li>
            <li> Calculate the required items.
            </p> </li>
            <li> Print the outputs/logs in .txt files (the outputs and the log file can be found in the "files" folder in this directory). </p> </li>
    </ol>  
    </p>
</body>

<img src="./css_estilos/hadoop_docker.drawio.png" style="float: center" width="600" height="558">

[<p style="font-family: rubik"> To Table of Contents </p> ](#id0)

---

<div id='id4' > </div>

<body>
    <h2> <b> Tools and Technologies </b> </h2>
    <p>
        <ul>
            <li> <b> <p> 
            Python Modules and Libraries
            </b>: 
                <ul>
                    <li> Datetime (module). </li>
                    <li> Dateutil (module). </li>
                    <li> Logging (module). </li>
                    <li> Lxml. </li>
                    <li> Operator (module). </li>
                    <li> Os (module). </li>
                    <li> Pathlib (module). </li>
                    <li> Pytest (module). </li>
                    <li> Re (module). </li>
                    <li> Statistics (module). </li>
                    <li> Xml (module). </li>
                </ul>
            </p> </li>
        </ul>
    </p>
</body>

<body>
    <p>
    The libraries used can be found at .txt file:
    <br>
    </p>
</body>

[<p style="font-family: rubik"> Requirements </p> ](requirements.txt)

[<p style="font-family: rubik"> To Table of Contents </p> ](#id0)

---

<div id='id5' > </div>

<body>
    <h2> <b> Metadata Repository </b> </h2>
    <p>
    To access metadata repository click here:
    </p>
</body>

[<p style="font-family: rubik"> Metadata Repository </p>](metadata_repository.txt)

[<p style="font-family: rubik"> To Table of Contents </p> ](#id0)

---

<div id='id6' > </div>

<body>
    <h2> <b> How to Run Main Program </b> </h2>
    <p>
    Open the working directory and from the main folder:
    <ol>
        <li> <p> Open the command terminal. </p> </li>
        <li> <p> Access the main folder of the working directory. </p> </li>
        <li> <p> Call the Python interpreter. </p> </li> 
        <li> <p> Execute the following command `core/main.py.` </p> </li>
    </ol>
    </p>
    <h2> <b> How to Run the Unit Tests </b> </h2>
    <p>
    Open the working directory and from the main folder:
    <ol>
        <li> <p> Open the command terminal. </p> </li>
        <li> <p> Access the main folder of the working directory. </p> </li>
        <li> <p> Call the Python interpreter. </p> </li> 
        <li> <p> Execute the following command `pytest core/test_main.py.` </p> </li>
    </ol>
    </p>
</body>

[<p style="font-family: rubik"> To Table of Contents </p> ](#id0)
