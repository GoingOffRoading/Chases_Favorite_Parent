# Chases_Favorite_Parent

For a time, I would crack jokes to my parents that I was the favorite child.  One of my parents didn't think this was as funny as I thought it was, and asked me to stop... Fine!  I can stop...  But I can't promise that I'm going to handle it like a well rounded & mature adult!

Chases_Favorite_Parent is a silly self-hosted Python Flask app that searches a directory (say, a directory full of pictures of your parents) for a random image and displays it:

![example.png from the repo](example.png)

The random component is intentional so that the app remains relatively innocent/cheeky.  

---

# How to use

## Mount the image folder

'/static/images/' is the directory for the photos



# What if I want to modify the HTML for 'my-favorite-sibling' or 'my-favorite-child'?

That makes us bothers.

- Clone the repo
- Modify lines 6 and 18 in the '/templates/index.html' to reflect the desired messaging.
- Build the container image (i.e. 'docker build -t favorite -f dockerfile .' or etc)
- Deploy the image you crazy animal


---

# Todo

- [x] Automate building the container image to GitHub
- [ ] Add more CSS to make the display pretty
- [ ] Add deployment instructions
- [ ] Add a Kubernetes/DockerCompose deployment example

