var chosen_language; // should never be changed

/**
 * 
 * @param {String} language 
 */
function setChosenLanguage(language) {
  this.chosen_language = language;
}

function getChosenLanguage() {
  return this.chosen_language;
}
