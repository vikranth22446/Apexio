import React, {Component} from 'react';
import Header from "./Header";

import {makeStyles} from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles({
    table: {
        marginLeft: '10px',
        marginRight: '10px',
        border: '5px solid transparent'
    },
});


function createData(name, calories, fat, carbs, protein) {
    return {name, calories, fat, carbs, protein};
}

const rows = [
    createData('Frozen yoghurt', 159, 6.0, 24, 4.0),
    createData('Ice cream sandwich', 237, 9.0, 37, 4.3),
    createData('Eclair', 262, 16.0, 24, 6.0),
    createData('Cupcake', 305, 3.7, 67, 4.3),
    createData('Gingerbread', 356, 16.0, 49, 3.9),
];

function DenseTable() {
    const classes = useStyles();

    return (
        <TableContainer component={Paper}>
            <Table className={classes.table} size="small" aria-label="a dense table">
                <TableHead>
                    <TableRow>
                        <TableCell>Has</TableCell>
                        <TableCell>Equals</TableCell>
                        <TableCell>Begins With</TableCell>
                        <TableCell>Extension</TableCell>
                        <TableCell>Regex</TableCell>
                        <TableCell>Move to</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {props.rows.map(row => (
                        <TableRow key={row.name}>
                            <TableCell component="th" scope="row">
                                {row.name}
                            </TableCell>
                            <TableCell>{row.has}</TableCell>
                            <TableCell>{row.equals}</TableCell>
                            <TableCell> {row.begins_with}</TableCell>
                            <TableCell>{row.extension}</TableCell>
                            <TableCell>{row.regex}</TableCell>
                            <TableCell>{row.moveTo}</TableCell>

                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}


class Rules extends Component {
    constructor(props) {
        super(props);

        this.state = {
            rows: []
        }
    }

    componentDidMount() {

        fetch('http://127.0.0.1:4242/get_all_rules').
        then(response => response.json())
            .then((jsonData) => {
                // jsonData is parsed json object received from url
                // console.log(jsonData);
                this.setState({rows: jsonData['rows']})
            })
            .catch((error) => {
                // handle your errors here
                console.error(error)
            })
    }

    render() {
        return (
            <div>
                <Header/>
                Rules:
                <div style={{marginRight: "30px", marginLeft: "30px"}}>
                    <DenseTable rows={this.state.rows}/>
                </div>
            </div>
        );
    }
}

export default Rules;