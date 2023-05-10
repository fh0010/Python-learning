print("Here's an Mad Libs story for you to fill in : \nTitle: The [adjective] [noun] [verb] to the [adjective] [noun]")
adj = input("Enter your first adjective here : ")
adj1 = input("Enter your second adjective here : ")
noun = input("Enter your first noun here : ")
noun1 = input("Enter your second noun here : ")
verb = input("Enter your verb here : ")

print("\n\nHere is your input : "+adj, adj1, noun, noun1, verb +"\n\n\n")

story = """Once upon a time, there was a {adj} {noun} who decided to {verb} to the {adj1}
 {noun1}. Along the way, they met a {adj} {noun1} who offered to {verb} with them. As they 
 walked, they saw a {adj1} {noun} in the distance, so they decided to {verb} towards it. 
 When they arrived, they were surprised to see a {adj} {noun1} inside. They decided to 
 {verb} it, and inside they found a {adj} {noun1} that had been {verb} for centuries. They 
 took it with them and continued on their journey. Eventually, they arrived at the {adj1} 
 {noun}, where they {verb} the {adj1} {noun1} and lived happily ever after.\n"""

filled_story = story.format(adj=adj, noun=noun, verb=verb, adj1=adj1, noun1=noun1) 

print(filled_story)
