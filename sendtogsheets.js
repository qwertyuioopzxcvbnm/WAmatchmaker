// Define the sheet name at the top of the script
const sheetName = 'Sheet1';

// This function initializes the script properties by storing the spreadsheet ID.
function initialSetup() {
  const activeSpreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  const sheetId = activeSpreadsheet.getId();
  Logger.log(sheetId); // Log the Spreadsheet ID for verification
  PropertiesService.getScriptProperties().setProperty('key', sheetId);
}

// Main function to handle POST requests and write form data to the Google Sheet.
function doPost(e) {
    Logger.log(e.parameters); // Log received parameters
    const sheetName = 'Sheet1'; 
    const lock = LockService.getScriptLock();
    lock.waitLock(10000);

    try {
        const scriptProp = PropertiesService.getScriptProperties();
        const docId = scriptProp.getProperty('key');

        if (!docId) {
            throw new Error('Spreadsheet ID is not set');
        }

        const doc = SpreadsheetApp.openById(docId);
        const sheet = doc.getSheetByName(sheetName);

        if (!sheet) {
            throw new Error('Sheet not found');
        }

        const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
        const nextRow = sheet.getLastRow() + 1;

        const newRow = headers.map(function(header) {
            if (header === 'Date') {
                return new Date();
            } else if (Array.isArray(e.parameter[header])) {
                return e.parameter[header].join(', '); // Convert array to comma-separated string
            } else if (typeof e.parameter[header] === 'string' && e.parameter[header].includes(',')) {
                return e.parameter[header]; // Already a comma-separated string
            } else {
                return e.parameter[header] || '';
            }
        });

        sheet.getRange(nextRow, 1, 1, newRow.length).setValues([newRow]);

        return ContentService
            .createTextOutput(JSON.stringify({ 'result': 'success', 'row': nextRow }))
            .setMimeType(ContentService.MimeType.JSON);

    } catch (error) {
        Logger.log(`Error encountered: ${error.message}`);
        return ContentService
            .createTextOutput(JSON.stringify({ 'result': 'error', 'error': error.message }))
            .setMimeType(ContentService.MimeType.JSON);
    } finally {
        lock.releaseLock();
    }
}