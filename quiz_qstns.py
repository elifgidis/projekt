'''
List of questions for each topics with correct answers to be compared for score calculation later.
'''

quiz_data = {
    'Science': [
        {"question": "What is the rarest blood type?",
         "options": ["A: AB negative", "B: O positive", "C: B negative", "D: A positive"],
         "correct_answer": "A: AB negative"},
        {"question": "“For every action, there is an equal and opposite reaction.” Which of Newton’s Laws states this?",
         "options": ["A: The first law of motion", "B: The second law of motion", "C: The third law of motion", "D: The law of universal gravitation"],
         "correct_answer": "C: The third law of motion"},
        {"question": "How many hearts does a worm have?",
         "options": ["A: 5", "B: 1", "C: 10", "D: 0"],
         "correct_answer": "A: 5"},
        {"question": "Name the tallest type of grass.",
         "options": ["A: Wheat", "B: Rice", "C: Bamboo", "D: Sugarcane"],
         "correct_answer": "C: Bamboo"},
        {"question": "How many bones do sharks have?",
         "options": ["A: 100", "B: 206", "C: 0", "D: 300"],
         "correct_answer": "C: 0"},
        {"question": "What is the measurement (which is approximately six feet) used to measure the depth of water?",
         "options": ["A: Meter", "B: Fathom", "C: Foot", "D: Yard"],
         "correct_answer": "B: Fathom"},
        {"question": "Which is the first organism to grow back after a fire?",
         "options": ["A: Grass", "B: Trees", "C: Moss", "D: Flowers"],
         "correct_answer": "C: Moss"},
        {"question": "How much weight can an ant lift?",
         "options": ["A: 10 times its own weight", "B: 20 times its own weight", "C: 50 times its own weight", "D: 100 times its own weight"],
         "correct_answer": "C: 50 times its own weight"},
        {"question": "When in groups, this jungle animal is referred to as an ambush. What kind of animal is this?",
         "options": ["A: Lion", "B: Elephant", "C: Tiger", "D: Gorilla"],
         "correct_answer": "C: Tiger"},
        {"question": "An average human takes how many breaths in a day?",
         "options": ["A: 10,000", "B: 15,000", "C: 23,000", "D: 30,000"],
         "correct_answer": "C: 23,000"},
        {"question": "What is the chemical symbol for water?",
         "options": ["A: CO2", "B: H2O", "C: O2", "D: NaCl"],
         "correct_answer": "B: H2O"},
        {"question": "Which is the smallest planet in the solar system?",
         "options": ["A: Mars", "B: Venus", "C: Mercury", "D: Earth"],
         "correct_answer": "C: Mercury"},
        {"question": "Which gas do plants absorb from the atmosphere during the process of photosynthesis?",
         "options": ["A: Oxygen", "B: Carbon dioxide", "C: Nitrogen", "D: Hydrogen"],
         "correct_answer": "B: Carbon dioxide"},
        {"question": "What is the chemical symbol for oxygen?",
         "options": ["A: O", "B: O2", "C: Ox", "D: O3"],
         "correct_answer": "A: O"},
        {"question": "What is the force that pulls objects toward the center of the Earth?",
         "options": ["A: Magnetism", "B: Gravity", "C: Friction", "D: Inertia"],
         "correct_answer": "B: Gravity"},
        {"question": "What is the study of fossils called?",
         "options": ["A: Archaeology", "B: Anthropology", "C: Paleontology", "D: Geology"],
         "correct_answer": "C: Paleontology"},
        {"question": "What is the name of the process by which plants make their own food using sunlight?",
         "options": ["A: Cellular respiration", "B: Metabolism", "C: Photosynthesis", "D: Fermentation"],
         "correct_answer": "C: Photosynthesis"},
        {"question": "What is the basic unit of life?",
         "options": ["A: Atom", "B: Molecule", "C: Cell", "D: Organism"],
         "correct_answer": "C: Cell"},
        {"question": "Which gas makes up the majority of Earth’s atmosphere?",
         "options": ["A: Oxygen", "B: Hydrogen", "C: Carbon dioxide", "D: Nitrogen"],
         "correct_answer": "D: Nitrogen"},
        {"question": "What is the process by which an organism changes over a period of time in response to its environment?",
         "options": ["A: Mutation", "B: Evolution", "C: Natural selection", "D: Adaptation"],
         "correct_answer": "B: Evolution"},
        {"question": "Which planet is often referred to as Earth’s “sister planet” due to its similar size and composition?",
         "options": ["A: Mars", "B: Jupiter", "C: Venus", "D: Saturn"],
         "correct_answer": "C: Venus"}
    ],
    'Literature': [
        {"question": "Which character from a classic work of fiction was born on September 22, 1290?",
         "options": ["A: Hobbit Bilbo Baggins", "B: Harry Potter", "C: Frodo Baggins", "D: Gandalf"],
         "correct_answer": "A: Hobbit Bilbo Baggins"},
        {"question": "Who created Pinocchio?",
         "options": ["A: Walt Disney", "B: Carlo Collodi", "C: Charles Perrault", "D: Hans Christian Andersen"],
         "correct_answer": "B: Carlo Collodi"},
        {"question": "Who is the author of Gremlins?",
         "options": ["A: Roald Dahl", "B: J.K. Rowling", "C: Stephen King", "D: C.S. Lewis"],
         "correct_answer": "A: Roald Dahl"},
        {"question": "What is the name of Long John Silver’s parrot in The Treasure Island?",
         "options": ["A: Polly", "B: Captain Flint", "C: Skippy", "D: Jack"],
         "correct_answer": "B: Captain Flint"},
        {"question": "Which author created Brer Rabbit?",
         "options": ["A: Mark Twain", "B: Joel Chandler Harris", "C: Beatrix Potter", "D: Aesop"],
         "correct_answer": "B: Joel Chandler Harris"},
        {"question": "Who is the author of The Graveyard, the 2009 Newbery award-winning book?",
         "options": ["A: J.K. Rowling", "B: Rick Riordan", "C: Neil Gaiman", "D: John Green"],
         "correct_answer": "C: Neil Gaiman"},
        {"question": "Which animal does Alice try to play croquet with in Alice’s Adventures in Wonderland?",
         "options": ["A: A flamingo", "B: A hedgehog", "C: A rabbit", "D: A caterpillar"],
         "correct_answer": "A: A flamingo"},
        {"question": "In the New Moon, Cullens tells everyone they are moving to which city?",
         "options": ["A: Los Angeles", "B: New York", "C: Seattle", "D: Forks"],
         "correct_answer": "A: Los Angeles"},
        {"question": "Who created Tarzan in 1914?",
         "options": ["A: J.M. Barrie", "B: Lewis Carroll", "C: Edgar Rice Burroughs", "D: Rudyard Kipling"],
         "correct_answer": "C: Edgar Rice Burroughs"},
        {"question": "What is the first name of Mr. Pickwick in The Pickwick Papers by Charles Dickens?",
         "options": ["A: Charles", "B: Samuel", "C: George", "D: John"],
         "correct_answer": "B: Samuel"},
        {"question": "Which classic novel tells the story of a young girl named Scout Finch?",
         "options": ["A: Pride and Prejudice", "B: The Great Gatsby", "C: To Kill A Mockingbird by Harper Lee", "D: Wuthering Heights"],
         "correct_answer": "C: To Kill A Mockingbird by Harper Lee"},
        {"question": "Who wrote the Percy Jackson & The Olympians series?",
         "options": ["A: J.K. Rowling", "B: Suzanne Collins", "C: Rick Riordan", "D: Christopher Paolini"],
         "correct_answer": "C: Rick Riordan"},
        {"question": "What is the title of the first book in J.R.R. Tolkien’s The Lord Of The Rings trilogy?",
         "options": ["A: The Two Towers", "B: The Return of the King", "C: The Fellowship Of The Ring", "D: The Silmarillion"],
         "correct_answer": "C: The Fellowship Of The Ring"},
        {"question": "Who wrote the dystopian novel 1984?",
         "options": ["A: Aldous Huxley", "B: George Orwell", "C: Ray Bradbury", "D: Philip K. Dick"],
         "correct_answer": "B: George Orwell"},
        {"question": "What is the name of the book series by Suzanne Collins that follows the adventures of Katniss Everdeen?",
         "options": ["A: Divergent", "B: The Maze Runner", "C: The Hunger Games", "D: Twilight"],
         "correct_answer": "C: The Hunger Games"},
        {"question": "Who wrote the fantasy novel The Hobbit?",
         "options": ["A: J.K. Rowling", "B: J.R.R. Tolkien", "C: C.S. Lewis", "D: George R.R. Martin"],
         "correct_answer": "B: J.R.R. Tolkien"},
        {"question": "What is the name of Elizabeth Bennet’s silly younger sister who elopes with Mr. Wickham?",
         "options": ["A: Mary Bennet", "B: Jane Bennet", "C: Lydia Bennet", "D: Catherine Bennet"],
         "correct_answer": "C: Lydia Bennet"},
        {"question": "Who is the author of The Fault in Our Stars, a novel about two teenagers stricken by cancer?",
         "options": ["A: Veronica Roth", "B: John Green", "C: Suzanne Collins", "D: Nicholas Sparks"],
         "correct_answer": "B: John Green"},
        {"question": "Who wrote the Divergent book series?",
         "options": ["A: Veronica Roth", "B: J.K. Rowling", "C: Rick Riordan", "D: Suzanne Collins"],
         "correct_answer": "A: Veronica Roth"},
        {"question": "In which book does a teenage boy named Holden Caulfield narrate his experiences in New York City?",
         "options": ["A: The Great Gatsby", "B: The Catcher In The Rye", "C: A Separate Peace", "D: Lord of the Flies"],
         "correct_answer": "B: The Catcher In The Rye"},
        {"question": "What is the name of the wizarding school in the Percy Jackson & The Olympians series?",
         "options": ["A: Hogwarts School of Witchcraft and Wizardry", "B: Beauxbatons Academy of Magic", "C: Camp Half-Blood", "D: Durmstrang Institute"],
         "correct_answer": "C: Camp Half-Blood"}
    ],
     'History and General Knowledge': [
        {"question": "What is the Roman name for the Goddess Hecate?",
         "options": ["A: Venus", "B: Diana", "C: Minerva", "D: Trivia"],
         "correct_answer": "D: Trivia"},
        {"question": "Who was the first president of the United States to live in the White House?",
         "options": ["A: George Washington", "B: John Adams", "C: Thomas Jefferson", "D: James Madison"],
         "correct_answer": "B: John Adams"},
        {"question": "Name the first country to use postcards.",
         "options": ["A: United Kingdom", "B: Germany", "C: France", "D: Australia"],
         "correct_answer": "D: Australia"},
        {"question": "In which year was the first all-electronic TV demonstrated by Philo T. Farnsworth?",
         "options": ["A: 1927", "B: 1930", "C: 1925", "D: 1935"],
         "correct_answer": "A: 1927"},
        {"question": "In which year did Christopher Columbus discover the “New World”?",
         "options": ["A: 1492", "B: 1500", "C: 1489", "D: 1512"],
         "correct_answer": "A: 1492"},
        {"question": "In which year did the Titanic sink?",
         "options": ["A: 1912", "B: 1910", "C: 1905", "D: 1915"],
         "correct_answer": "A: 1912"},
        {"question": "New York City was originally known by which Dutch name?",
         "options": ["A: New Holland", "B: Nieuw Amsterdam", "C: Amsterdam New", "D: New Rotterdam"],
         "correct_answer": "B: Nieuw Amsterdam"},
        {"question": "Which Filipino was named the Iron Butterfly?",
         "options": ["A: Corazon Aquino", "B: Gloria Macapagal Arroyo", "C: Imelda Marcos", "D: Leila de Lima"],
         "correct_answer": "C: Imelda Marcos"},
        {"question": "Where was Napoleon Bonaparte born?",
         "options": ["A: Paris, France", "B: Corsica, France", "C: Marseille, France", "D: Lyon, France"],
         "correct_answer": "B: Corsica, France"},
        {"question": "Who was the first President of the United States?",
         "options": ["A: George Washington", "B: John Adams", "C: Thomas Jefferson", "D: James Madison"],
         "correct_answer": "A: George Washington"},
        {"question": "Who is known for leading the nonviolent civil rights movement in the United States during the 1950s and 1960s?",
         "options": ["A: Malcolm X", "B: Rosa Parks", "C: Martin Luther King Jr.", "D: Frederick Douglass"],
         "correct_answer": "C: Martin Luther King Jr."},
        {"question": "What ancient civilization built the pyramids in Egypt?",
         "options": ["A: The Romans", "B: The Greeks", "C: The Mesopotamians", "D: The Ancient Egyptians"],
         "correct_answer": "D: The Ancient Egyptians"},
        {"question": "Which event marked the beginning of World War-I in 1914?",
         "options": ["A: The Battle of Verdun", "B: The assassination of Archduke Franz Ferdinand", "C: The signing of the Treaty of Versailles", "D: The invasion of Poland"],
         "correct_answer": "B: The assassination of Archduke Franz Ferdinand"},
        {"question": "Who was the name of the famous nurse during the Crimean War known for her work in improving medical practices?",
         "options": ["A: Clara Barton", "B: Florence Nightingale", "C: Mary Seacole", "D: Edith Cavell"],
         "correct_answer": "B: Florence Nightingale"},
        {"question": "Who was the leader of the Soviet Union during the Cuban Missile Crisis?",
         "options": ["A: Leonid Brezhnev", "B: Joseph Stalin", "C: Mikhail Gorbachev", "D: Nikita Khrushchev"],
         "correct_answer": "D: Nikita Khrushchev"},
        {"question": "Who is known for inventing the printing press around 1440?",
         "options": ["A: Leonardo da Vinci", "B: Galileo Galilei", "C: Johannes Gutenberg", "D: Isaac Newton"],
         "correct_answer": "C: Johannes Gutenberg"},
        {"question": "Who was the famous Native American woman who helped the Lewis and Clark expedition as a guide?",
         "options": ["A: Pocahontas", "B: Sacagawea", "C: Lozen", "D: Sarah Winnemucca"],
         "correct_answer": "B: Sacagawea"},
        {"question": "What was the name of the ship that carried the Pilgrims to North America in 1620?",
         "options": ["A: The Mayflower", "B: The Santa Maria", "C: The Nina", "D: The Pinta"],
         "correct_answer": "A: The Mayflower"},
        {"question": "What ancient wonder of the world was a giant statue located on the Greek island of Rhodes?",
         "options": ["A: The Lighthouse of Alexandria", "B: The Colossus of Rhodes", "C: The Statue of Zeus at Olympia", "D: The Great Pyramid of Giza"],
         "correct_answer": "B: The Colossus of Rhodes"},
        {"question": "Who is known for his theory of evolution?",
         "options": ["A: Isaac Newton", "B: Albert Einstein", "C: Charles Darwin", "D: Gregor Mendel"],
         "correct_answer": "C: Charles Darwin"}
    ],
    'Geography': [
    {"question": "What is the capital of France?",
     "options": ["A: Berlin", "B: Madrid", "C: Paris", "D: Rome"],
     "correct_answer": "C: Paris"},
    {"question": "Which country has the largest area?",
     "options": ["A: China", "B: United States", "C: Canada", "D: Russia"],
     "correct_answer": "D: Russia"},
    {"question": "What river is the longest in the world?",
     "options": ["A: Amazon", "B: Nile", "C: Yangtze", "D: Mississippi"],
     "correct_answer": "B: Nile"},
    {"question": "Which desert is the largest in the world?",
     "options": ["A: Sahara", "B: Arabian", "C: Gobi", "D: Kalahari"],
     "correct_answer": "A: Sahara"},
    {"question": "What is the smallest country in the world?",
     "options": ["A: Monaco", "B: Nauru", "C: Vatican City", "D: San Marino"],
     "correct_answer": "C: Vatican City"},
    {"question": "Which continent is the largest by land area?",
     "options": ["A: Africa", "B: Asia", "C: Europe", "D: North America"],
     "correct_answer": "B: Asia"},
    {"question": "What is the longest mountain range in the world?",
     "options": ["A: Andes", "B: Himalayas", "C: Rockies", "D: Alps"],
     "correct_answer": "A: Andes"},
    {"question": "Which country has the most islands in the world?",
     "options": ["A: Finland", "B: Norway", "C: Canada", "D: Sweden"],
     "correct_answer": "D: Sweden"},
    {"question": "What city is known as the City of Canals?",
     "options": ["A: Amsterdam", "B: Venice", "C: Bangkok", "D: Stockholm"],
     "correct_answer": "B: Venice"},
    {"question": "Which U.S. state is the Grand Canyon located in?",
     "options": ["A: Arizona", "B: Colorado", "C: New Mexico", "D: Utah"],
     "correct_answer": "A: Arizona"},
    {"question": "What is the capital of Australia?",
     "options": ["A: Sydney", "B: Perth", "C: Melbourne", "D: Canberra"],
     "correct_answer": "D: Canberra"},
    {"question": "Which country is known as the Land of the Rising Sun?",
     "options": ["A: China", "B: Japan", "C: South Korea", "D: Thailand"],
     "correct_answer": "B: Japan"},
    {"question": "What is the largest ocean on Earth?",
     "options": ["A: Atlantic", "B: Indian", "C: Southern", "D: Pacific"],
     "correct_answer": "D: Pacific"},
    {"question": "Mount Everest is located in which country?",
     "options": ["A: India", "B: Nepal", "C: Tibet", "D: China"],
     "correct_answer": "B: Nepal"},
    {"question": "What is the capital city of Spain?",
     "options": ["A: Barcelona", "B: Madrid", "C: Seville", "D: Valencia"],
     "correct_answer": "B: Madrid"},
    {"question": "Which river flows through London?",
     "options": ["A: Thames", "B: Seine", "C: Rhine", "D: Danube"],
     "correct_answer": "A: Thames"},
    {"question": "Which country is Prague the capital of?",
     "options": ["A: Czech Republic", "B: Slovakia", "C: Poland", "D: Hungary"],
     "correct_answer": "A: Czech Republic"},
    {"question": "What is the name of the largest lake in the world?",
     "options": ["A: Lake Superior", "B: Lake Victoria", "C: Caspian Sea", "D: Lake Baikal"],
     "correct_answer": "C: Caspian Sea"},
    {"question": "Which of these cities is not a national capital?",
     "options": ["A: Sydney", "B: Ottawa", "C: Helsinki", "D: Cairo"],
     "correct_answer": "A: Sydney"},
    {"question": "What country has the longest coastline?",
     "options": ["A: United States", "B: Russia", "C: Canada", "D: Australia"],
     "correct_answer": "C: Canada"},
    {"question": "Which country is bordered by both the Atlantic and Indian Oceans?",
     "options": ["A: Brazil", "B: South Africa", "C: Australia", "D: India"],
     "correct_answer": "B: South Africa"}
],
'English ': [
    {"question": "What part of speech describes a verb, adjective, or adverb and answers when? where? how? and to what extent?",
     "options": ["A: Noun", "B: Pronoun", "C: Adverb", "D: Preposition"],
     "correct_answer": "C: Adverb"},
    {"question": "Which sentence is in the passive voice?",
     "options": ["A: The cat chased the mouse.", "B: The mouse was chased by the cat.", "C: The cat chases the mouse.", "D: The cat had chased the mouse."],
     "correct_answer": "B: The mouse was chased by the cat."},
    {"question": "What is the past tense form of 'run'?",
     "options": ["A: Ran", "B: Runned", "C: Running", "D: Run"],
     "correct_answer": "A: Ran"},
    {"question": "Which of the following is a coordinating conjunction?",
     "options": ["A: And", "B: Because", "C: Although", "D: Which"],
     "correct_answer": "A: And"},
    {"question": "What is the plural form of 'mouse'?",
     "options": ["A: Mouses", "B: Mice", "C: Mouse", "D: Meese"],
     "correct_answer": "B: Mice"},
    {"question": "Which word is an example of a possessive pronoun?",
     "options": ["A: They", "B: Their", "C: Them", "D: Themselves"],
     "correct_answer": "B: Their"},
    {"question": "What type of sentence is this: 'Do you know where my shoes are?'",
     "options": ["A: Declarative", "B: Imperative", "C: Interrogative", "D: Exclamatory"],
     "correct_answer": "C: Interrogative"},
    {"question": "Which of these words is an example of an indefinite article?",
     "options": ["A: The", "B: A", "C: An", "D: This"],
     "correct_answer": "B: A"},
    {"question": "Identify the correct spelling.",
     "options": ["A: Accomodation", "B: Accommodation", "C: Acomodation", "D: Acommodation"],
     "correct_answer": "B: Accommodation"},
    {"question": "Which sentence correctly uses a semicolon?",
     "options": ["A: I have a big test tomorrow; I can't go out tonight.", "B: I have a big test tomorrow, I can't go out tonight.", "C: I have a big test tomorrow: I can't go out tonight.", "D: I have a big test tomorrow - I can't go out tonight."],
     "correct_answer": "A: I have a big test tomorrow; I can't go out tonight."},
    {"question": "What is the direct object in the sentence 'She sold her car'?",
     "options": ["A: She", "B: Sold", "C: Her", "D: Car"],
     "correct_answer": "D: Car"},
    {"question": "Which of the following sentences is correct?",
     "options": ["A: Its a beautiful day.", "B: It's a beautiful day.", "C: Its' a beautiful day.", "D: It's a beautiful day's."],
     "correct_answer": "B: It's a beautiful day."},
    {"question": "Identify the subjective (nominative) pronoun in the sentence: 'He and I went to the store.'",
     "options": ["A: He", "B: I", "C: He and I", "D: Store"],
     "correct_answer": "C: He and I"},
    {"question": "Which of the following is an example of an interjection?",
     "options": ["A: Wow!", "B: On", "C: Beautiful", "D: Run"],
     "correct_answer": "A: Wow!"},
    {"question": "What is the correct way to write a possessive form of 'Chris'?",
     "options": ["A: Chris'", "B: Chris's", "C: Chrises", "D: Chris"],
     "correct_answer": "B: Chris's"},
    {"question": "Which sentence uses 'their' correctly?",
     "options": ["A: Their going to the beach tomorrow.", "B: I love their new house.", "C: They're books are on the shelf.", "D: Its their turn to clean."],
     "correct_answer": "B: I love their new house."},
    {"question": "What is the past participle form of 'eat'?",
     "options": ["A: Ate", "B: Eat", "C: Eaten", "D: Eating"],
     "correct_answer": "C: Eaten"},
    {"question": "Which sentence is correctly punctuated?",
     "options": ["A: The family's car is very old.", "B: The familys' car is very old.", "C: The families car is very old.", "D: The families' car is very old."],
     "correct_answer": "A: The family's car is very old."},
    {"question": "In the sentence 'Quickly running, she barely caught the bus,' what is 'Quickly'?",
     "options": ["A: Adjective", "B: Noun", "C: Adverb", "D: Preposition"],
     "correct_answer": "C: Adverb"},
    {"question": "Which sentence correctly uses 'to', 'too', and 'two'?",
     "options": ["A: I want too eat two pieces of cake, to.", "B: I want to eat too pieces of cake, too.", "C: I want to eat two pieces of cake, too.", "D: I want too eat to pieces of cake, two."],
     "correct_answer": "C: I want to eat two pieces of cake, too."}
],'Technology': [
    {"question": "Who is known as the father of computers?",
     "options": ["A: Charles Babbage", "B: Alan Turing", "C: John Atanasoff", "D: Bill Gates"],
     "correct_answer": "A: Charles Babbage"},
    {"question": "What does 'HTTP' stand for?",
     "options": ["A: HyperText Transfer Product", "B: HyperTransfer Text Protocol", "C: HyperText Transfer Protocol", "D: HyperTransfer Text Product"],
     "correct_answer": "C: HyperText Transfer Protocol"},
    {"question": "Which company developed the video game Fortnite?",
     "options": ["A: Activision", "B: Epic Games", "C: Electronic Arts", "D: Ubisoft"],
     "correct_answer": "B: Epic Games"},
    {"question": "What is the name of the first successful personal computer?",
     "options": ["A: IBM PC", "B: Apple Macintosh", "C: Commodore PET", "D: Apple II"],
     "correct_answer": "D: Apple II"},
    {"question": "In what year was the first iPhone released?",
     "options": ["A: 2005", "B: 2007", "C: 2009", "D: 2006"],
     "correct_answer": "B: 2007"},    {"question": "What does 'CPU' stand for?",
     "options": ["A: Central Processing Unit", "B: Computer Personal Unit", "C: Central Personal Unit", "D: Central Processor Unit"],
     "correct_answer": "A: Central Processing Unit"},
    {"question": "Which language is primarily used for Android app development?",
     "options": ["A: Java", "B: Swift", "C: Kotlin", "D: C#"],
     "correct_answer": "C: Kotlin"},
    {"question": "What is the name of the world's first computer programmer?",
     "options": ["A: Charles Babbage", "B: Ada Lovelace", "C: Alan Turing", "D: Bill Gates"],
     "correct_answer": "B: Ada Lovelace"},
    {"question": "Which of these is not an operating system?",
     "options": ["A: Linux", "B: MacOS", "C: Android", "D: Oracle"],
     "correct_answer": "D: Oracle"},
    {"question": "What year was the World Wide Web introduced to the public?",
     "options": ["A: 1989", "B: 1991", "C: 1993", "D: 1995"],
     "correct_answer": "B: 1991"},
    {"question": "Which company invented the floppy disk?",
     "options": ["A: IBM", "B: Microsoft", "C: Apple", "D: Sony"],
     "correct_answer": "A: IBM"}

],'Sports': [
    {"question": "Which country hosted the 2016 Summer Olympics?",
     "options": ["A: China", "B: Brazil", "C: United Kingdom", "D: Russia"],
     "correct_answer": "B: Brazil"},
    {"question": "Who holds the record for most goals in FIFA World Cup history?",
     "options": ["A: Pele", "B: Miroslav Klose", "C: Ronaldo", "D: Lionel Messi"],
     "correct_answer": "B: Miroslav Klose"},
    {"question": "What sport is known as 'the sport of kings'?",
     "options": ["A: Polo", "B: Horse Racing", "C: Fencing", "D: Archery"],
     "correct_answer": "B: Horse Racing"},
    {"question": "Which country won the first ever FIFA World Cup in 1930?",
     "options": ["A: Uruguay", "B: Brazil", "C: Germany", "D: Argentina"],
     "correct_answer": "A: Uruguay"},
    {"question": "In tennis, what piece of fruit is found at the top of the men's Wimbledon trophy?",
     "options": ["A: Apple", "B: Pineapple", "C: Strawberry", "D: Grape"],
     "correct_answer": "B: Pineapple"},  
    {"question": "How many players are on a soccer field for one team during a match?",
     "options": ["A: 9", "B: 10", "C: 11", "D: 12"],
     "correct_answer": "C: 11"},
    {"question": "In golf, what name is given to a hole score of one under par?",
     "options": ["A: Eagle", "B: Birdie", "C: Bogey", "D: Ace"],
     "correct_answer": "B: Birdie"},
    {"question": "Which country is traditionally known as the birthplace of sumo wrestling?",
     "options": ["A: China", "B: Japan", "C: South Korea", "D: Mongolia"],
     "correct_answer": "B: Japan"},
    {"question": "Who is known as 'The Great One' in ice hockey?",
     "options": ["A: Mario Lemieux", "B: Wayne Gretzky", "C: Sidney Crosby", "D: Alexander Ovechkin"],
     "correct_answer": "B: Wayne Gretzky"},
    {"question": "What sport is played at Wimbledon?",
     "options": ["A: Cricket", "B: Tennis", "C: Golf", "D: Soccer"],
     "correct_answer": "B: Tennis"},
    {"question": "What is the only country to have played in every single soccer World Cup?",
     "options": ["A: Brazil", "B: Germany", "C: Argentina", "D: Italy"],
     "correct_answer": "A: Brazil"}

     ], 'Art and Culture': [
    {"question": "Who painted the Mona Lisa?",
     "options": ["A: Vincent Van Gogh", "B: Leonardo da Vinci", "C: Michelangelo", "D: Raphael"],
     "correct_answer": "B: Leonardo da Vinci"},
    {"question": "Which city is known as the art capital of the world?",
     "options": ["A: Paris", "B: New York", "C: London", "D: Florence"],
     "correct_answer": "A: Paris"},
    {"question": "What is the literary term for a play on words?",
     "options": ["A: Metaphor", "B: Simile", "C: Pun", "D: Hyperbole"],
     "correct_answer": "C: Pun"},
    {"question": "In Greek mythology, who is the god of music, poetry, and the sun?",
     "options": ["A: Zeus", "B: Apollo", "C: Hermes", "D: Ares"],
     "correct_answer": "B: Apollo"},
    {"question": "The Louvre Museum is located in which city?",
     "options": ["A: Rome", "B: Madrid", "C: Paris", "D: London"],
     "correct_answer": "C: Paris"},
    {"question": "Which famous artist cut off his own ear?",
     "options": ["A: Pablo Picasso", "B: Vincent Van Gogh", "C: Claude Monet", "D: Leonardo da Vinci"],
     "correct_answer": "B: Vincent Van Gogh"},
    {"question": "In which country is the ancient city of Petra located?",
     "options": ["A: Jordan", "B: Egypt", "C: Israel", "D: Syria"],
     "correct_answer": "A: Jordan"},
    {"question": "The Sistine Chapel ceiling was painted by which artist?",
     "options": ["A: Leonardo da Vinci", "B: Michelangelo", "C: Raphael", "D: Donatello"],
     "correct_answer": "B: Michelangelo"},
    {"question": "Shakespeare's Hamlet is the prince of which country?",
     "options": ["A: Denmark", "B: England", "C: Scotland", "D: Norway"],
     "correct_answer": "A: Denmark"},
    {"question": "What musical period is Ludwig van Beethoven associated with?",
     "options": ["A: Baroque", "B: Classical", "C: Romantic", "D: Renaissance"],
     "correct_answer": "C: Romantic"},
    {"question": "Which novel is the famous line 'It was the best of times, it was the worst of times' from?",
     "options": ["A: War and Peace", "B: A Tale of Two Cities", "C: Great Expectations", "D: Moby Dick"],
     "correct_answer": "B: A Tale of Two Cities"}

]





}
