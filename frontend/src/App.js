import { Typography, Button } from "@mui/material";
import React, { useState } from "react";

function App() {
  const [file, setFile] = useState();

  function handleChange(event) {
    setFile(event.target.files[0]);
  }

  function handleSubmit(event) {
    event.preventDefault();

    var formdata = new FormData();
    formdata.append("sampleFile", file);
    formdata.append("fileName", file.name)

    var requestOptions = {
      method: "POST",
      mode: "no-cors",
      body: formdata,
      redirect: "follow",
    };

    fetch("http://localhost:1337/upload", requestOptions)
      .then((response) => {
        console.log(response)
        // response.json()
      })
      // .then((result) => {
        // console.log(result)
      // })
      .catch((error) => console.log("error", error));
  }

  return (
    <div className="App">
      <Typography variant="h2" sx={{ textAlign: "center" }}>
        De-makeup Project
      </Typography>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleChange} />
        <Button type="submit">Upload</Button>
      </form>
      <img src="http://localhost:1337/get_original_img"></img>
    </div>
  );
}

export default App;
