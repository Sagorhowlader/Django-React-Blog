import {
    LOAD_POST_SUCCESS,
    LOAD_POST_FAIL
} from '../actions/types';



const initialState = {
    userPostsList: []
};
export default function(state = initialState, action) {
    
    const { type, payload } = action;
   

    switch(type) {
        case LOAD_POST_SUCCESS:
            console.log(payload)
            return {
                userPostsList: [...state.userPostsList,payload]
            //  userPostsList: [...state.userPostsList,payload.post]
            }
        case LOAD_POST_FAIL:
            return {
                ...state,
                userPostsList: []
            }
        default:
            return state
    };
};