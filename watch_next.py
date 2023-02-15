# importing spacy
import spacy

# Loading the model and assigning it to the variable nlp
nlp = spacy.load('en_core_web_md')


# Defining function movie_similarity
def movie_similarity(description):
    model_description = nlp(description)

    # Creating a dictionary smilarity_list to store  movie name and similarity scores.
    similarity_list = {}

    # Using dictionary movie tite and description, finding the similarity score between the descriptions in list and hulk description
    for title, descrip in movies_descrip.items():
        similarity = nlp(descrip).similarity(model_description)
        similarity_list[title] = similarity

    # Finding the maximum value and using for loop for to find respective movie name
    max_value = max(similarity_list.values())
    for title, similarity in similarity_list.items():
        if similarity == max_value:

            # returning suggestion as which movie a user would watch next
            print(f"The most similar movie is: {title}")

# Creating a dictionary movie_descrip to store  movie name and its description.
movies_descrip = {}
with open('movies.txt', 'r') as file:
    movies = file.readlines()
    for movie in movies:
        split_data = movie.strip().split(" :")
        movies_descrip[split_data[0]] = split_data[1]

# Storing the hulk movie descriptionas planet_hulk_description
planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"

# Calling function movie similarity and as parameter planet_hulk_description
movie_similarity(planet_hulk_description)


# print(description[float(max(similarity_list))])