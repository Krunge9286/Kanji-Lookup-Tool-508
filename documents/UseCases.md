# Week 1 Milestone: Use Cases

For my project, I want to make a Japanese kanji look-up tool. These are the use cases as of right now:

### 1.	Provide basic information about the kanji such as meaning, readings, stroke count, etc. This is what just about every kanji lookup tool can do at a minimum.
Example input:  
海  
Output:   
Meaning: sea; ocean  
Kunyomi readings: うみ  
Onyomi readings: カイ  
Nanori readings: あ、あま、うな、うん、え、か、た、ひろ、ひろし、ぶ、まち、まま、み、め、わたる  
Stroke count: 9  
etc.  

### 2.	Return a list of kanji that match the mora, or syllable(s) entered by the user. So, basically the opposite of the previous use case. On my tool, I only want it to return kanji that have a mora which matches the user’s input exactly.  
Example input:  
ka (or か or カ)  
Output:  
kanji such as 下, 化, and 家 that have ka itself as a reading, but NOT kanji such as 高, which has taka as a reading but not ka.  
Furthermore, I want it to be able to filter by type of reading based on the user’s input. So, if a user searches ka under “nanori reading,” it will return the kanji 海, but otherwise this kanji will not be returned.  

### 3.	Return the maximum and minimum “efficiency” scores of a kanji.  
This takes the maximum and minimum number of mora that can be pronounced with a single kanji, and divides each by the kanji’s stroke count to get two different numbers. In other words, how many sounds can this kanji make compared to how complex the written form is.  
Example input:   
海   
(This kanji has 9 strokes, and can produce 3 mora at maximum and 1 at minimum.)  
Output:  
Max efficiency score: 0.333  
Min efficiency score: 0.111  

### 4.	Show the Unicode for the inputted kanji along with the rest of the information about the kanji.  

### 5.	Allow users to mark a given kanji with personal labels such as “learned,” “learning,” and “haven’t learned yet.” Users could even label large groups of kanji (by their JLPT level, for instance) all at once. 
