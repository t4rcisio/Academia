import Box from "@mui/material/Box";
import Checkbox from "@mui/material/Checkbox";
import FormControlLabel from "@mui/material/FormControlLabel";
import Frequencia from "../Frequency";

import "./style.css";

export default function Secretary() {
  return (
    <form className="schedulesRegister-main" onSubmit={""}>
      <Box>
        <h2>Modalidades</h2>
        <Box sx={{ minWidth: 150 }}>
          <FormControlLabel control={<Checkbox />} label="Musculação" />
          <Frequencia />
        </Box>

        <Box sx={{ minWidth: 150 }}>
          <FormControlLabel control={<Checkbox />} label="Natação" />
          <Frequencia />
        </Box>

        <Box sx={{ minWidth: 150 }}>
          <FormControlLabel control={<Checkbox />} label="Crossfit" />
          <Frequencia />
        </Box>

        <Box sx={{ minWidth: 150 }}>
          <FormControlLabel control={<Checkbox />} label="Spinning" />
          <Frequencia />
        </Box>

        <Box sx={{ minWidth: 150 }}>
          <FormControlLabel control={<Checkbox />} label="Ritmos" />
          <Frequencia />
        </Box>
      </Box>
    </form>
  );
}
