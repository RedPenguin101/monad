# The Monad Project

The goal of the Monad Project is to create a personal knowledge base for me.

The basic element of the knowledge base is the *Monad* - a basic unit of knowledge. A Monad should be *small* (like a chunk in the learning how to learn course). A monad should belong to a monad library, a collection of monads which are intimately connected. (though all monads should ultimately be connected through some degree of separation due to the interconnectness of all knowledge) 

Monad.py:
The Monad Class, which has a title and text. The text should in time be replaced by a series of widgets, including:
	* Text Widget (this should have a sub-widget, markdown with LaTeX integration)
	* Timeline Widget
	* Image widget
	* tag widget
	* quiz / recall widget, with questions for spaced repetition
	* practice widgets: stuff that allows you to practice the theory of what is in the Monad. also part of spaced repetition, including mixing it up for interleaving
	* quotes widget: relevant quotes from book
	* Citations and sources widget

functions for:
	* encode and decode monad to JSON format.
	* get_monad_list: reads the monad master and returns a list of monads
	* commit_monad: takes a monad as an argument and adds it to the monad master
	* create_monad_CLI: a function for creating monads from the command line
	
Plans for the future:
1. Write some Monads
2. Create 'version control' functionality, where you can look at the history of a monad
2. Implement widgets 
2. Create a simple viewer (in either Urwid or web based using Flask)
3. Monads will dynamically connect together based on tags or content 
4. A spaced repetition module, where flashcards associated with the monad are given at spaced intervals
5. The ability to create memory palace entries
6. A random daily article function, where once a day a monad is sent to you (the probability of a monad being selected increases based on the time since last review)
7. You can tag things in a monad for elaboration (i.e. flag to create a new Monad from)
8. There is a 'todo' list of monads that need to be written
9. Some sort of version of that Burroughs method of writing where he cut up a bunch of words and shuffled them - goal is to put different ideas together in unpredictable ways (maybe some way to 'cross' monads, a short narrative on similar ideas between two disparate monads?)
10. a diffuse mode facilitator - though no idea what that would look like.
11. Some kind of pomodoro implementation.
