import random

def play_mad_libs():
	print("\nWelcome to Mad Libs! Let's make a funny story.")




def story_one():
	print("\n--- Mad Lib #1: A Day at the Zoo ---")
	noun = input("Enter a noun: ")
	adjective = input("Enter an adjective: ")
	verb = input("Enter a verb ending in -ing: ")
	animal = input("Enter an animal: ")

story = (
f"Today I went to the zoo and saw a {adjective} {animal} "
f"{verb} next to a huge {noun}! It was the craziest thing ever!"
)
print("\nYour Story:")
print(story)


def story_two():
	print("\n--- Mad Lib #2: The Crazy School Day ---")
	teacher = input("Enter your teacher's name: ")
	food = input("Enter a type of food: ")
	adjective = input("Enter an adjective: ")
	verb = input("Enter a past-tense verb: ")

story = (
f"In class today, {teacher} brought in {food} for everyone. "
f"It smelled so {adjective} that the whole class {verb}!"
)

print("\nYour Story:")
print(story)


def story_three():
	print("\n--- Mad Lib #3: Space Adventure ---")
	planet = input("Enter the name of a planet: ")
	adjective = input("Enter an adjective: ")
	sound = input("Enter a funny sound: ")
	creature = input("Enter a made-up creature: ")

	story = (
	f"While visiting {planet}, I met a {adjective} alien that said '{sound}' "
	f"before riding away on a {creature}!"
	)

stories = [story_one, story_two, story_three]
chosen_story = random.choice(stories)
chosen_story()
print("\nYour Story:")
print(story)


if __name__ == "__main__":
	play_mad_libs()
	