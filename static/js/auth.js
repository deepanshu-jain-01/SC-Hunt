import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import {
  getAuth,
  GoogleAuthProvider,
  signInWithPopup,
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
const provider = new GoogleAuthProvider(app);

// Google Button On Sign In Page --------------------->
const googleLogin1 = document.getElementById("login1");

googleLogin1.addEventListener("click", function (event) {
  event.preventDefault();

  signInWithPopup(auth, provider)
    .then((result) => {
      const credential = GoogleAuthProvider.credentialFromResult(result);
      const user = result.user;
      const uid = user.uid;
      window.location.href = `/index/${uid}`;
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
    });
});


// Google Button on Create an Account Page:
const googleLogin11 = document.getElementById("login11");

googleLogin11.addEventListener("click", function (event) {
  event.preventDefault();

  signInWithPopup(auth, provider)
    .then((result) => {
      const credential = GoogleAuthProvider.credentialFromResult(result);
      const user = result.user;
      const uid = user.uid;
      window.location.href = `/index/${uid}`;
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
      alert(errorMessage);
    });
});
