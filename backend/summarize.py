import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from heapq import nlargest

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Remove stopwords (common words that do not contribute much to the meaning)
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Calculate word frequency
    word_freq = FreqDist(words)

    # Assign a score to each sentence based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence):
            if word.lower() in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word.lower()]
                else:
                    sentence_scores[sentence] += word_freq[word.lower()]

    # Get the top N sentences with the highest scores
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Join the selected sentences to create the summary
    summary = ' '.join(summary_sentences)

    return summary

if __name__ == "__main__":
    # Example text to summarize
    input_text = """
In the heart of the bustling city, where the cacophony of car horns and the symphony of chatter create a relentless urban soundtrack, there exists a hidden oasis of tranquility. Tucked away between towering skyscrapers and nondescript storefronts, the city park is a green haven, an escape from the concrete jungle that surrounds it. The park's entrance is marked by a wrought-iron gate adorned with intricate, swirling patterns that seem to whisper of an earlier, more elegant time.

As you step through the gate, the world outside fades away. Tall trees line meandering pathways, their branches forming a natural canopy that dapples the ground with patches of sunlight. The air is alive with the chirping of birds and the gentle rustle of leaves. A serpentine stream winds its way through the park, its waters shimmering in the dappled sunlight. Ducks paddle lazily, leaving ripples in their wake, while children giggle and chase after them, their laughter a joyful counterpoint to the serenity of the scene.

Beneath the shade of a centuries-old oak tree, a solitary figure sits on a weathered bench, lost in thought. The bench has witnessed countless such moments of contemplation over the years, its wooden slats bearing the marks of time and the stories of those who have sat upon it. The figure, an elderly man with a lined face and a shock of white hair, gazes out at a pond where lilies bloom, their delicate petals a stark contrast to the rugged stones that border the water's edge.

Beyond the pond, a gazebo stands at the park's center, an elegant structure of wrought iron and wood, its ornate columns and latticework giving it an air of timeless beauty. It is a popular spot for weddings and romantic rendezvous, where vows are exchanged and promises made amid the backdrop of nature's serenity.

As you wander deeper into the park, you encounter pockets of activity and solitude. A group of yoga enthusiasts has gathered in a secluded glade, their mats arranged in a circle as they seek harmony with both body and nature. Nearby, a solitary artist sits on a stool, a canvas perched on an easel, capturing the play of light on the park's foliage with deft strokes of a paintbrush.

The park is a tapestry of stories, a place where people of all walks of life come to seek respite, inspiration, or simply a moment of solitude. It is a testament to the enduring power of nature to provide solace and inspiration amidst the chaos of the modern world. In this urban oasis, where the city's relentless energy is hushed to a gentle hum, one can find a sense of peace and renewal that transcends the boundaries of time and place.
    """

    num_sentences_in_summary = 2
    summarized_text = summarize_text(input_text, num_sentences_in_summary)
    print("Summarized Text:")
    print(summarized_text)
