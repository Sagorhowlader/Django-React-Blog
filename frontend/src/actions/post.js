import Cookies from 'js-cookie';
import axios from 'axios';
import {
    LOAD_POST_SUCCESS,
    LOAD_POST_FAIL
} from './types';

export const load_Post = () => async dispatch => {
    const config = {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    };

    try {
        const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/all-post-view`, config);
        
        if (res.data.error) {
           
            dispatch({
                type: LOAD_POST_FAIL
            });
        } else {
            dispatch({
                type: LOAD_POST_SUCCESS,
                payload: res.data
            });
        }
    } catch (err) {
        dispatch({
            type: LOAD_POST_FAIL
        });
    }
};
