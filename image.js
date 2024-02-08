const fs = require('fs');
const path = require('path');

// Specify the path to your images folder
const folderPath = './';

// Create an array to store image variables
const images = [];

// Read the contents of the folder
fs.readdir(folderPath, (err, files) => {
    if (err) {
        console.error('Error reading folder:', err);
        return;
    }

    // Filter files with specific image extensions (e.g., .jpg, .png)
    const imageExtensions = ['.jpg', '.jpeg', '.png', '.gif'];
    const imageFiles = files.filter(file => imageExtensions.includes(path.extname(file).toLowerCase()));

    // Iterate over image files
    imageFiles.forEach(imageFile => {
        // Create an image variable or use the file path directly
        const imagePath = path.join(folderPath, imageFile);
        images.push({
            name: path.basename(imagePath),
            path: imagePath,
            // Add other properties as needed
        });

        // Optionally, log the image details
        console.log('Added image:', path.basename(imagePath));
    });

    // Now, 'images' array contains image variables
    console.log('Images array:', images);
    console.log(`${imageFiles[2]}`);
});
