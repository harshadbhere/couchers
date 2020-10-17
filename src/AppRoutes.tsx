import React, { useEffect } from "react";
import { Switch, Route, RouteProps, Redirect } from "react-router-dom";
import Home from "./views/Home";
import Profile from "./views/Profile";
import Messages from "./views/Messages";
import Login from "./views/Login";
import { useDispatch, useSelector } from "react-redux";
import { RootState } from "./reducers";
import { authError } from "./features/auth/authSlice";
import Logout from "./views/Logout";

export const loginRoute = "/login";
export const loginPasswordRoute = loginRoute + "/password";
export const loginSentRoute = loginRoute + "/sent";

export const profileRoute = "/profile";
export const messagesRoute = "/messages";
export const requestsRoute = "/messages";
export const logoutRoute = "/logout";

export default function AppRoutes() {
  return (
    <Switch>
      <Route path={`${loginRoute}/:urlToken?`}>
        <Login />
      </Route>
      <PrivateRoute path={profileRoute}>
        <Profile />
      </PrivateRoute>
      <PrivateRoute path={messagesRoute}>
        <Messages />
      </PrivateRoute>
      <PrivateRoute exact path="/">
        <Home />
      </PrivateRoute>
      <PrivateRoute exact path={logoutRoute}>
        <Logout />
      </PrivateRoute>
    </Switch>
  );
}

// TODO: Redirect to requested route after login
const PrivateRoute = (props: RouteProps) => {
  const dispatch = useDispatch();
  const isAuthenticated = useSelector<RootState, boolean>(
    (state) => state.auth.authToken != null
  );
  useEffect(() => {
    if (!isAuthenticated) {
      dispatch(authError("Please log in."));
    }
  });

  const { children, ...otherProps } = props;

  return (
    <>
      <Route {...otherProps}>
        {!isAuthenticated && <Redirect to="/login" />}
        {children}
      </Route>
    </>
  );
};
