const nodemailer = require('nodemailer');
const ExcelJS = require('exceljs');
const fs = require('fs');
const path = require('path');

// Specify the path to your images folder
const folderPath = './reciepts/';

// Specify the path to your Excel file
const excelFilePath = 'adhyaaya24registeration.xlsx';
const adhyaaya24registeration = new ExcelJS.adhyaaya24registeration();

// Create a transporter using your email service provider's SMTP settings
const transporter = nodemailer.createTransport({
  service: 'gmail', // Use the appropriate service (e.g., 'gmail', 'yahoo', 'outlook', etc.)
  auth: {
    user: 'adhyaaya.gcoen@gmail.com',
    pass: 'jbeo kvvd eony eokq',
  },
});

// Create an array to store image variables
const images = [];

// Read the contents of the folder
fs.readdir(folderPath, (err, files) => {
  if (err) {
    console.error('Error reading folder:', err);
    return;
  }

  // Filter files with specific image extensions (e.g., .jpg, .jpeg, .png)
  const imageExtensions = ['.jpg', '.jpeg', '.png', '.gif'];
  const imageFiles = files.filter(file => imageExtensions.includes(path.extname(file).toLowerCase()));

  // Iterate over image files
  imageFiles.forEach(imageFile => {
    const imagePath = path.join(folderPath, imageFile);
    images.push({
      name: path.basename(imagePath),
      path: imagePath,
    });

    console.log('Added image:', path.basename(imagePath));
  });

  // Read data from the Excel file
  adhyaaya24registeration.xlsx.readFile(excelFilePath)
    .then(() => {
      // Assuming you have a single sheet in the workbook
      const worksheet = adhyaaya24registeration.getWorksheet(1);
      let index = 0;

      // Iterate over rows and columns
      worksheet.eachRow({ includeEmpty: false }, (row, rowNumber) => {
        console.log(`Row ${rowNumber}: ${row.getCell(1).value}, ${row.getCell(2).value}, ${row.getCell(3).value}`);

        // Create mail options for each row
        const mailOptions = {
          from: 'adhyaaya.gcoen@gmail.com',
          to: 'yashbalpande40@gmail.com',
          subject: `Successful Registration Confirmation - {{Event Name}}`,
          text: `${row.getCell(2).value}, ${row.getCell(3).value}, ${row.getCell(4).value}`,
          attachments: [
            {
              filename: images[index].name,
              path: images[index].path,
              cid: `image_${index + 1}`, // Optional: Unique identifier for the image in the email body
            },
          ],
        };

        index++;

        // Send the email for each row
        transporter.sendMail(mailOptions, (error, info) => {
          if (error) {
            console.error('Error sending email:', error);
          } else {
            console.log('Email sent:', info.response);
          }
        });
      });
    })
    .catch(error => {
      console.error('Error reading Excel file:', error);
    });
});
