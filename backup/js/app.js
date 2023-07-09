/*import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
  // The value of `databaseURL` depends on the location of the database
  databaseURL: "https://console.firebase.google.com/u/1/project/ovd-research-project/database/ovd-research-project-default-rtdb/data/~2F",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);


// to write to the DB
function writeUserData(userId, gender, birthYear, country, favColor, colorblind, howLongUsesWeb, howOftenUsesWeb, howOftenBrowseShops, lastYearOnlinePurchases) {
    const db = getDatabase();
    set(ref(db, 'preQuestionnaireForUser/' + userId), {
      gender: gender,
      birthYear: birthYear,
      country : country,
      favColor : favColor,
      colorblind : colorblind,
      howLongUsesWeb : howLongUsesWeb,
      howOftenUsesWeb : howOftenUsesWeb,
      howOftenBrowseShops : howOftenBrowseShops,
      lastYearOnlinePurchases : lastYearOnlinePurchases
    });
  }

  */
