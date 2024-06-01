import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import {
  getAuth,
  signInWithEmailAndPassword,
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

const s_submit = document.getElementById("s_submit");

s_submit.addEventListener("click", function (event) {
  event.preventDefault();

  const s_email = document.getElementById("s_email").value;
  const s_password = document.getElementById("s_password").value;

  signInWithEmailAndPassword(auth, s_email, s_password)
    .then((userCredential) => {
      const user = userCredential.user;
      const uid = user.uid;
      const displayName = user.displayName;
      const email = user.email;
      
      // const user_dict = { displayName: displayName, email: email, uid: uid};
      // localStorage.setItem("user_dict", JSON.stringify(user_dict));

      window.location.href = `/index/${uid}`;
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
      alert(errorMessage);
    });
});
