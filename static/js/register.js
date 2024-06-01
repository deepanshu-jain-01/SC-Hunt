import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import {
  getAuth,
  createUserWithEmailAndPassword,
  updateProfile,
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

const c_submit = document.getElementById("c_submit");
c_submit.addEventListener("click", function (event) {
  event.preventDefault();

  const c_email = document.getElementById("c_email").value;
  const c_password = document.getElementById("c_password").value;
  const c_name = document.getElementById("c_name").value;

//   createUserWithEmailAndPassword(auth, c_email, c_password)
//     .then((userCredential) => {
//       const user = userCredential.user;
//       const uid = user.uid;
//       window.location.href = `/index/${uid}`;
//       return updateProfile(user, { displayName: c_name });
//     })
//     .catch((error) => {
//       const errorCode = error.code;
//       const errorMessage = error.message;
//       alert(errorMessage);
//     });
// });

createUserWithEmailAndPassword(auth, c_email, c_password)
  .then((userCredential) => {
    const user = userCredential.user;
    const uid = user.uid;
    const uname = user.displayName;
    const uemail = user.email;

    window.location.href = `/index/${uid}`;
    return updateProfile(user, { displayName: c_name })
      .then(() => {
        // Add the fetch request here
        const user_dict = { displayName: uname, email: uemail, uid: uid};
  
        fetch('/api/user_details', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(user_dict)
        })
        .then(response => response.json())
        .then(result => console.log(result))
        .catch(error => console.log('Error: ', error));
      });
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    alert(errorMessage);
  });
});
