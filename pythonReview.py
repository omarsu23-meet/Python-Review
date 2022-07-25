def create_youtube_video(title, description):
	dic = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
	return dic

def like(youtube_video):
	if 'likes' in youtube_video:
		youtube_video['likes'] += 1
	return youtube_video

def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video['dislikes'] += 1
	return youtube_video


def add_comment(youtubevideo, username, comment_text):
	youtubevideo['comments'][username] = comment_text
	return


vid = create_youtube_video('cool cat', 'i like my cat')

vid = like(vid)

for x in range(495):
	vid = like(vid)

print(vid)

print('what is your username: ')
username = input()
print('give us a comment: ')
comments = input()

add_comment(vid, username, comments)
print(vid)