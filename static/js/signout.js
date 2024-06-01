import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import {
  getAuth,
  signOut,
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

const signout = document.getElementById("signout");
signout.addEventListener("click", function (event) {
  event.preventDefault();
  signOut(auth)
    .then(() => {
      window.location.href = "/";
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
    });
});
