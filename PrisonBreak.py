#Prison Break

print("""
	The Prison Game
	The object of this game is to escape the prison without being caught.
  Ready to begin? (y/n)
  """)
choice = input()
if choice == 'y':
	cell()
else:
	quit

def prison_title():
	print("""
		##################################################
		#      PPPPP RRRRR IIIII SSSSS  OOO  N    N      #			 
		#      P   P R   R   I   S     O   O N N  N      #					 
		#      PPPPP RRRRR   I   SSSSS O   O N  N N      #			 
		#      P     R  R    I       S O   O N   NN      #		 
		#      P     R   R IIIII SSSSS  OOO  N    N      #		 
		##################################################
				""")

def cell():
	prison_title()
	print("""
		You are in a prison cell. You've been here for 20 years for a crime you
		did not commit, and need to get out. There are some dirty bed sheets,
		a mirror by the sink, and the cell door is locked.

	  Press S to inspect the Sheets
	  Press L to inspect the Lock
		Press M to inspect the Mirror
				""")
	choice = input()
	if choice == 's':
		sheets()
	elif choice == 'l':
		cell_lock()
	elif choice == 'm':
		mirror()

def cell_mirror():
	prison_title()
	print("""
		You are in your cell with the mirror. You wonder how you could use this to
		escape. The gross sheets are still on the bed, and the cell door is locked.
		
		Press S to inspect the Sheets
		Press L to inspect the Lock
				""")
	choice = input()
	if choice == 's':
		sheets_mirror()
	elif choice == 'l':
		cell_lock_mirror()

def sheets():
	prison_title()
	print("""
		There are filthy, disgusting sheets on the bed.
		You can't believe you actually sleep in these. That's prison life...

		Press R to Return to your cell
				""")

def sheets_mirror():
	prison_title()
	print("""
		You look at the same disgusting sheets again.
    Hopefully you won't have to look at them much longer.
    
    Press R to Return to your cell
				""")
	choice = input()
	if choice = 'r':
		cell_mirror()

def mirror():
	prison_title()
	print("""
		As you look into the mirror yet again after 20 years, you suddenly notice that
    the mirror looks a little strange. You are compelled to take a closer look...

    Press L to Look closer
    Press R to Return to your cell
				""")
	choice = input()
	if choice == 'l':
		mirror_look()
	elif choice == 'r':
		cell()

def mirror_look():
	prison_title()
	print("""
		When you look at it from another angle, you can see that the mirror is loose.
		It looks like you can take it.

		Press T to take the mirror
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 't':
		cell_mirror()
	elif choice == 'r':
		cell()

def cell_lock():
	prison_title()
	print("""
		It's one of those keypad locks. You have no idea what the combination is.
		You can't see the keypad from where you're standing. If you could look at it
		from the outside, you might be able to see which numbers were pressed by that
		slob guard's dirty hands.

		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'r':
		cell()

def cell_lock_mirror():
	prison_title()
	print("""
		It's one of those keypad locks. You have no idea what the combination is.
		Maybe now you can see which numbers were pressed by that slob guard's dirty hands.
		
		Press M to use Mirror
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'm':
		keypad()
	elif choice == 'r':
		cell_mirror()

def keypad():
	prison_title()
	print("""
		You reach your hand through the bars, and point the mirror back at the keypad.
		You can now see the combination to unlock it.
		
		Press K to use the Keypad
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'k':
		lock_open()
	elif choice == 'r':
		cell_mirror()

def lock_open():
	prison_title()
	print("""
		You escaped your cell! Now is your best chance to escape! There are some boxes
		to your left, and a closet door about 20 feet away. The hallway looks like it
		leads to some stairs.
		
		Press C to check the Closet
		Press S to check the Stairs
				""")
	choice = input()
	if choice == 'c':
		closet_locked()
	elif choice == 's':
		stairs()

def lock_open1():
	prison_title()
	print("""
		You are in the hallway outside the cell. The hallway leads to stairs, and
    there's a closet door about 20 feet away.

    Press C to check the Closet
    Press H to check the Hall
    Press S to check the Stairs
    """)
	choice = input()
	if choice == 'c':
		closet_locked1()
	elif choice == 'h':
		hall1()
	elif choice == 's':
		stairs()

def closet():
	prison_title()
	print("""
		Just as you reach for the doorknob, you hear a guard coming down the hall. Your
    heart is pounding in your chest as you start to panic. You need to hide!
    
    Press C to hide in the Closet
    Press B to hide behind the Boxes
    Press R to Return to your cell
    """)
	choice = input()
	if choice == 'c':
		closet_locked()
	elif choice == 'b':
		boxes()
	elif choice == 'r':
		cell_open()

def boxes():
	prison_title()
	print("""
		You hide behind the boxes as the guard closes in. He notices the cell door open
 		and runs over to inspect. It doesn't take him long to notice you behind the
    boxes. Before you know it, you're surrounded by guards. There is no escape.
 		The guards cuff you, and escort to the maximum security solitary cells. The head
 		guard says "There's no way you can escape now. You will die in this cell!"
 		
 		Press R to Restart the game
 		""")
	choice = input()	
	if choice == 'r':
		cell()

def cell_open():
	prison_title()
	print("""
		You are back in your cell. This should avoid suspicion from the gaurd.
		You sit on the bed with nasty sheets as the guards walks by. He takes a quick
		look in your cell, and walks back down the hall and up the stairs.
		
		Press S to inspect the Sheets
		Press H to go to the Hall
				""")
	choice = input()
	if choice == 's':
		sheets_gross()
	elif choice == 'h':
		hall()

def closet_locked():
	prison_title()
	print("""
		The closet door is locked. You might be able to pick the lock with something.
		The guard is still coming! You don't have much time!
	
		Press B to hide behind the Boxes
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'b':
		boxes()
	elif choice == 'r':
		cell_open()

def closet_locked1():
	prison_title()
	print("""
		The closet door is locked. You might be able to pick the lock with something.
    
    Press R to Return to the hall
				""")
	choice = input()
	if choice == 'r':
		hall()

def closet_locked2():
	prison_title()
	print("""
		The closet door is locked. You might be able to pick the lock with something.
    
    Press P to Pick the lock
    Press R to Return to the hall
				""")
	choice = input()
	if choice == 'p':
		closet_open()
	elif choice == 'r':
		hall2()

def closet_open():
	print("""
		You pick the lock with the hairpin. The hairpin breaks, but the closet door opens.

	  Press S to Search the closet
	  Press R to Return to the hall
				""")
	choice = input()
	if choice == 's':
		closet_open1()
	elif choice == 'r':
		hall3()

def closet_open1():
	print("""
		This closet is full of maintenance equipment. A spare janitor's uniform is hanging up.
		
		Press I to Inspect the uniform
		Press R to Return to the hall
		""")
	choice = input()
	if choice == 'i':
		uniform()
	elif choice == 'r':
		hall3()

def closet_open2():
	print("""
		This closet is full of maintenance equipment. Nothing else useful here.
		
		Press C to Change out of uniform
		Press R to Return to the hall
		""")
	choice = input()
	if choice == 'c':
		closet_open1()
	elif choice == 'r':
		hall4()

def open_closet():
	print("""
		The closet door is open.
		
		Press E to Enter the closet
		Press R to Return to the hall
		""")
	choice = input()
	if choice == 'c':
		closet_open1()
	elif choice == 'r':
		hall3()

def open_closet1():
	print("""
		The closet door is open.
		
		Press E to Enter the closet
		Press R to Return to the hall
		""")
	choice = input()
	if choice == 'c':
		closet_open2()
	elif choice == 'r':
		hall3()

def open_closet2():
	print("""
		The closet door is open.
		
		Press E to Enter the closet
		Press R to Return to the hall
		""")
	choice = input()
	if choice == 'c':
		closet_open2()
	elif choice == 'r':
		hall4()

def uniform():
	print("""
		This uniform looks to be about your size.
		
		Press W to Wear the uniform
		Press R to Return to the closet
				""")
	choice = input()
	if choice == 'w':
		closet_janitor()
	elif choice == 'r':
		closet_open1()

def closet_janitor():
	print("""
		You are now dressed as a janitor. This could be the perfect disguise.
		
		Press C Change out of the uniform
		Press R to Return to the closet
				""")
	choice = input()
	if choice == 'c':
		closet_open1()
	elif choice == 'r':
		closet_open2()

def stairs():
	print("""
		You peek up the stairs, and see 2 doors. One leading outside, and the other to
		the guard's office. Trying to escape now is just asking to get shot. Better come
		up with a plan.
		
		Press R to Return to the hall
				""")
	choice = input()
	if choice == 'r':
		hall()

def stairs1():
	print("""
		You peek up the stairs, and see 2 doors. One leading outside, and the other to
		the guard's office. All you are armed with is a hairpin. Trying to escape now
		is just asking to get shot. Better come up with a plan.
		
		Press R to Return to the hall
				""")
	choice = input()
	if choice == 'r':
		hall2()

def stairs2():
	print("""
		There are two doors upstairs. One leading outside, and the other to the guard's office.
		Being dressed as the janitor gives you the best chance yet to escape unnoticed.

		Press C to enter the Courtyard
		Press R to Return to the hall
				""")
	choice = input()
	if choice == 'c':
		courtyard()
	elif choice == 'r':
		hall4()

def sheets_gross():
	print("""
		Ugh! You wonder why you keep looking at these. You have to get out of here!
		
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'r':
		cell_final()

def hall():
	print("""
		You are in the hallway outside the cell. The hallway leads to stairs, and
		there's a closet door about 20 feet away.

		Press C to check the Closet
		Press H to check the Hall
		Press S to check the Stairs
				""")
	choice = input()
	if choice == 'c':
		closet()
	elif choice == 'h':
		hall()
	elif choice == 's':
		stairs()

def hall1():
	print("""
		As you search the hallway, you come across a hairpin. This might come in handy.

		Press T to Take the hairpin
		Press R to Return to the hall
				""")
	choice = input()
	if choice == 't':
		hall2() #return to hall with hairpin
	elif choice == 'r':
		hall() #return to hall w/o hairpin

def hall2():
	print("""
		You are in the hallway outside the cell. The hallway leads to stairs, and
    there's a closet door about 20 feet away.
    
    Press C to check the Closet
    Press S to check the Stairs
				""")
	choice = input()
	if choice == 'c':
		closet_locked2() #already checked once
	elif choice == 'r':
		stairs() #check the stairs (no guard)

def hall3():
	print("""
		You are back in the hallway. Looks like the stairs are your way out.
    
    Press C to check the Closet
    Press S to check the Stairs
				""")
	choice = input()
	if choice == 'c':
		open_closet() #
	elif choice == 's':
		stairs2() #

def hall4():
	print("""
		You are back in the hallway. Looks like the stairs are your way out.
    
    Press C to check the Closet
    Press S to check the Stairs
				""")
	choice = input()
	if choice == 'c':
		open_closet2() #
	elif choice == 's':
		stairs2() #

def cell_final():
	print("""
		Ok, this is it. The guard won't be back for a while, now is your last chance.
		You can almost feel the freedom.

		Press H to go to the Hallway.
				""")
	choice = input()
	if choice == 'h':
		hall() #

def courtyard():
	print("""
		Nervously, you start to climb the stairs. Your hearts is pounding! As you walk
	  by the office, you make eye contact with one of the guards. He says "Hey!"
	  and your heart stops.
	  
	  Press T to Talk to the guard
	  Press R to Run for it
				""")
	choice = input()
	if choice == 't':
		guard() #
	elif choice == 'r':
		run() #

def guard():
	print("""
		The guards says "Have a good night," and nods to you. You can't believe
    that actually worked!
    
    Press C to enter the Courtyard.
				""")
	choice = input()
	if choice == 'c':
		freedom() #

def run():
	print("""
		You panic and burst out the door as the guard chases you. The guard sounds the
	  alarm and signals to outside guards there's a prisoner on the loose. Both towers
	  have guns drawn on you as they take aim. The first bullet almost hits you in the
	  leg. 

	  You keep running. The gate is only 20 yards away, just a little further and
	  you're free! Suddenly, you fall to the ground as you feel your lower body go
	  completely numb. You've been shot. You can't move your legs. You take one last
	  look at the gate, just several feet away. You hear one final shot and everything
	  goes black.	  
				""")
	time.sleep(10)
	print("""
		Press R to Restart
			""")
	choice = input()
	if choice == 'r':
		cell() #

def freedom():
	print("""
		You wish the guard a good night, and enter the courtyard. Your heart
    is pounding out of your chest as you walk to the outer gate. You get to the
    gate, and look up at the tower.
    
    You think to yourself, "please open the gate..." The gate opens for you.
    You smile as you walk off the prison grounds. You are finally free!    
				""")
	time.sleep(10)
	print("""
		Press R to Restart
			""")
	choice = input()
	if choice == 'r':
		cell() #