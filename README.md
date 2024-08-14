# Text-to-Mp3-Convert

This project is a Python script that reads text data from an Excel file, translates Hindi text to English, and then converts both the Hindi and English text into audio files using Google Text-to-Speech (gTTS). The resulting audio files are saved in MP3 format.

## Features

- **Read Data from Excel:** The script reads the text data from a specified Excel file.
- **Translate Text:** The Hindi text is translated into English using the Google Translate API.
- **Text-to-Speech Conversion:** Both the original Hindi text and the translated English text are converted to speech and saved as MP3 files.
- **Naming Convention:** The MP3 files are named based on the row number and the name field from the Excel file, with a prefix to indicate the language (H for Hindi and E for English).

## Prerequisites

Before running the script, ensure you have the following Python packages installed:

- `pandas`
- `gTTS`
- `googletrans==4.0.0-rc1`

You can install these packages using `pip`:

```bash
pip install pandas gtts googletrans==4.0.0-rc1
```

## How to Use

1. **Prepare the Excel File:**
   - Ensure your Excel file (e.g., `source.xlsx`) contains at least two columns: `No`, `Name`, and `Information`.
   - The `No` column should have a unique identifier (e.g., a serial number).
   - The `Name` column should contain the name you want to associate with the audio files.
   - The `Information` column should contain the Hindi text that needs to be converted and translated.

2. **Run the Script:**
   - Place the Excel file in the same directory as your script.
   - Run the Python script:

   ```bash
   python script_name.py
   ```

3. **Output:**
   - The script will generate two MP3 files for each row in the Excel file:
     - `NoHName.mp3`: The Hindi version of the text.
     - `NoEName.mp3`: The English version of the translated text.

   For example, if `No` is `1` and `Name` is `Example`, the output files will be `1HExample.mp3` and `1EExample.mp3`.

## Example

Suppose your `source.xlsx` file has the following data:

| 0  | Gujarat | गुजरात, भारत का एक प्रमुख राज्य है जो अपनी ऐतिहासिक, सांस्कृतिक, और प्राकृतिक सुंदरता के लिए प्रसिद्ध है। यहां की प्रमुख विशेषताएं हैं विश्व प्रसिद्ध सोमनाथ और द्वारका मंदिर, गिर वन्य जीव अभयारण्य (एशिया का सबसे बड़ा), रणनी की वाव, और राणी की वाव जैसे ऐतिहासिक स्थल। गुजरात का मौसम गर्मियों में शांति और सर्दियों में मिलने वाली सूर्यास्त की अद्वितीय अनुभूति के लिए उत्तम है। यहां की स्थानीय खाना और भोजन, जैसे कि ढोकला, कांदा भजी, और धोकली विशेष पसंदीदा हैं। गुजरात की प्राकृतिक सुंदरता, सांस्कृतिक विविधता, और उनकी विश्वस्तरीय खासियतों ने इसे एक प्रमुख पर्यटन और व्यापारिक राज्य बना दिया है। यहां की समृद्ध इतिहास, संस्कृति, और विभिन्नता ने भारतीय और विदेशी पर्यटकों को खींचा है। गुजरात का दर्शन करना एक साहसिक और विविध अनुभव है, जो पर्यटकों को इस भारतीय राज्य की रमणीयता, धरोहर, और संस्कृति का अद्वितीय दर्शन प्रदान करता है।

After running the script, you will get the following files:

- `1HSample.mp3` (Hindi audio)
- `1ESample.mp3` (English audio)

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions, whether big or small, are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- This project uses the [Google Translate API](https://pypi.org/project/googletrans/) for text translation.
- The [gTTS library](https://pypi.org/project/gTTS/) is used for converting text to speech.
