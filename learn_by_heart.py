import re

original_text = """The Frost performs its secret ministry,
Unhelped by any wind. The owlet's cry
Came loud—and hark, again! loud as before.
The inmates of my cottage, all at rest,
Have left me to that solitude, which suits
Abstruser musings: save that at my side
My cradled infant slumbers peacefully.
'Tis calm indeed! so calm, that it disturbs
And vexes meditation with its strange
And extreme silentness. Sea, hill, and wood,
This populous village! Sea, and hill, and wood,
With all the numberless goings-on of life,
Inaudible as dreams! the thin blue flame
Lies on my low-burnt fire, and quivers not;
Only that film, which fluttered on the grate,

Still flutters there, the sole unquiet thing.
Methinks, its motion in this hush of nature
Gives it dim sympathies with me who live,
Making it a companionable form,
Whose puny flaps and freaks the idling Spirit
By its own moods interprets, every where
Echo or mirror seeking of itself,
And makes a toy of Thought.

                      But O! how oft,
How oft, at school, with most believing mind,
Presageful, have I gazed upon the bars,
To watch that fluttering stranger ! and as oft
With unclosed lids, already had I dreamt
Of my sweet birth-place, and the old church-tower,
Whose bells, the poor man's only music, rang
From morn to evening, all the hot Fair-day,
So sweetly, that they stirred and haunted me
With a wild pleasure, falling on mine ear
Most like articulate sounds of things to come!
So gazed I, till the soothing things, I dreamt,
Lulled me to sleep, and sleep prolonged my dreams!
And so I brooded all the following morn,
Awed by the stern preceptor's face, mine eye
Fixed with mock study on my swimming book:
Save if the door half opened, and I snatched
A hasty glance, and still my heart leaped up,
For still I hoped to see the stranger's face,
Townsman, or aunt, or sister more beloved,
My play-mate when we both were clothed alike!

         Dear Babe, that sleepest cradled by my side,
Whose gentle breathings, heard in this deep calm,
Fill up the intersperséd vacancies
And momentary pauses of the thought!
My babe so beautiful! it thrills my heart
With tender gladness, thus to look at thee,
And think that thou shalt learn far other lore,
And in far other scenes! For I was reared
In the great city, pent 'mid cloisters dim,
And saw nought lovely but the sky and stars.
But thou, my babe! shalt wander like a breeze
By lakes and sandy shores, beneath the crags
Of ancient mountain, and beneath the clouds,
Which image in their bulk both lakes and shores
And mountain crags: so shalt thou see and hear
The lovely shapes and sounds intelligible
Of that eternal language, which thy God
Utters, who from eternity doth teach
Himself in all, and all things in himself.
Great universal Teacher! he shall mould
Thy spirit, and by giving make it ask.

         Therefore all seasons shall be sweet to thee,
Whether the summer clothe the general earth
With greenness, or the redbreast sit and sing
Betwixt the tufts of snow on the bare branch
Of mossy apple-tree, while the night-thatch
Smokes in the sun-thaw; whether the eave-drops fall
Heard only in the trances of the blast,
Or if the secret ministry of frost
Shall hang them up in silent icicles,
Quietly shining to the quiet Moon.
"""


def remove_word_body(text):
    remove_posses = re.sub(r"'s", ' ', text)
    output = re.sub('\\B\w', ' ', remove_posses)
    return(output)


def numerate_text(text_str):
    numerated_list = []
    split_text = text_str.split("\n")
    n_lines = len(split_text)
    max_digits = len(str(n_lines+1))

    for i in range(len(split_text)):
        if (i+1) % 5 != 0:
            line = ''.join([' ' for i in range(max_digits+2)])+split_text[i]
        else:
            digits = len(str(i+1))
            line = str(
                i+1) + ''.join([' ' for i in range(max_digits+2-digits)]) +\
                split_text[i]
        numerated_list.append(line)
    numerated_text = "\n".join(numerated_list)
    return(numerated_text)


transformed_text = remove_word_body(original_text)
num_trans_text = numerate_text(transformed_text)
num_original_text = numerate_text(original_text)


output_text = "\n\n".join([num_trans_text, num_original_text])

file_name = original_text[0:15]+'_transformed_text.txt'

with open(file_name, 'w') as out_file:
    out_file.write(output_text)
