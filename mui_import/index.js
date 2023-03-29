import {Button, TextField} from '@mui/material';

import { createTheme, ThemeProvider } from '@mui/material/styles';

export const theme = createTheme({});

export default function MyApp() {
  return (
    <ThemeProvider theme={theme}>
      <TextField />
      <Button>Hello World</Button>
    </ThemeProvider>
  );
}