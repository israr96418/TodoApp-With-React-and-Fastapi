import './App.css'
import { AppBar, Toolbar, Button, Box, TableContainer, Table, TableBody, TableCell, TextField, TableRow } from '@material-ui/core'
import { useState } from 'react';
import axios from 'axios'

function App() {
  const [users, setUsers] = useState([]);
  const [user, setUser] = useState({});

  const fetchusers = async ()=>{
    const response = await axios.get("http://localhost:8000/")
    console.log("fetch data from backend: ",response)
    return setUsers(response.data)
  }
  // fetchusers()
   
  const fetchuser = async(id)=>{
    const response = await axios.get(`http://localhost:8000/${id}`)
    return setUser(response.data)
  }

  const createorEdituser = async()=>{
    if(user.id){
      await axios.put(`http://localhost:8000/${user.id}`,user)
    }else{
      await axios.post(`http://localhost:8000/`,user)
    }
    await fetchusers()
    await setUser({id:0, name:"", email:"", password:""})

  }
  const deleteuser = async(id)=>{
    await axios.delete(`http://localhost:8000/${id}`)
    await fetchusers()
    // return setUsers(respone.data)
  }


  return (
    <div>
      <AppBar position="static">
        <Toolbar>
          <Button color="inherit">User</Button>
        </Toolbar>
    </AppBar>
        <Box m={10}>
          <TableContainer>
          <TextField value={user.id} type= "hidden" />
            <Table aria-label="simple table">

              <TableBody>
                <TableRow>
                  <TableCell>
                    <TextField value={user.name} onChange={(e)=>setUser({...user, name:e.target.value})} id='standard_basic' label="Name" />
                  </TableCell>
                  <TableCell>
                    <TextField value={user.email} onChange={(e)=>setUser({...user, email:e.target.value})} id='standard_basic' label="Email" />
                  </TableCell>
                  <TableCell>
                    <TextField value={user.password} onChange={(e)=>setUser({...user, password:e.target.value})} id='standard_basic' label="Password" />
                  </TableCell>
                  <TableCell>
                    <Button onClick={()=> createorEdituser()} variant='contained' color='primary'>
                      Submit
                    </Button>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell>Name</TableCell>
                  <TableCell>Email</TableCell>
                  <TableCell>Password</TableCell>
                  <TableCell>Edit</TableCell>
                  <TableCell>Delete</TableCell>
                </TableRow>
                {users.map((row) => (
                  <TableRow key={row.id}>
                    <TableCell>{row.name}</TableCell>
                    <TableCell>{row.email}</TableCell>
                    <TableCell>{row.password}</TableCell>
                    <TableCell>
                      <Button onClick={()=>fetchuser(row.id)} variant='contained' color='primary'>
                        Edit
                      </Button>
                    </TableCell>
                    <TableCell>
                      <Button onClick={()=>deleteuser(row.id)} variant='contained' color='secondry'>
                        Delete
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </Box>
    </div>
  )
}

export default App
