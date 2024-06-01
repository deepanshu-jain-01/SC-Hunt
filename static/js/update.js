import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import {
  getAuth,
  onAuthStateChanged,
} from "https://www.gstatic.com/firebasejs/10.11.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyANUu2C65iiPdbZ2OhhBVf_N2hICAfZ0nk",
  authDomain: "schunt-oauth.firebaseapp.com",
  projectId: "schunt-oauth",
  storageBucket: "schunt-oauth.appspot.com",
  messagingSenderId: "248905597152",
  appId: "1:248905597152:web:179d03211f918b524f9085",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const user = auth.currentUser;

function updateUserProfile(user) {
  const uname = user.displayName;
  const uemail = user.email;
  const upic = user.photoURL;
  const uid = user.uid;

  const user_dict = { displayName: uname, email: uemail, uid: uid};
  localStorage.setItem("user_dict", JSON.stringify(user_dict));

  // fetch('/api/user_details', {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type':'application/json'
  //   },
  //   body: JSON.stringify(user_dict)
  // })
  // .then(response => response.json)
  // .then(result => console.log(result))
  // .catch(error => console.log('Error: ',error))

  document.getElementById("uname").textContent = uname;
  document.getElementById("uemail").textContent = uemail;
  if (upic) {
    document.getElementById("upic").src = upic;
  } else {
    // If the user doesn't have a profile picture, use a default one
    document.getElementById("upic").src =
      "../static/assets/user_default_icon.png";
  }
}

onAuthStateChanged(auth, (user) => {
  if (user) {
    updateUserProfile(user);
    const uid = user.uid;
    return uid;
  } else {
  }
});


